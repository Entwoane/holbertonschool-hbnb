/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  const API_BASE_URL = 'http://127.0.0.1:3000';
  const loginForm = document.getElementById('login-form');

  checkAuthentication();

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      let isValid = true;

      if (email === '' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        document.getElementById('emailError').textContent =
          'Please enter a valid email address.';
        isValid = false;
      } else {
        document.getElementById('emailError').textContent = '';
      }

      if (password === '') {
        document.getElementById('passwordError').textContent =
          'Please enter a valid password.';
        isValid = false;
      } else {
        document.getElementById('passwordError').textContent = '';
      }

      if (!isValid) return;

      async function loginUser(email, password) {
        try {
          const response = await fetch(`${API_BASE_URL}/api/v1/auth/login`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password }),
          });

          if (response.ok) {
            const data = await response.json();
            document.cookie = `token=${data.access_token}; path=/; max-age=3600`;
            window.location.href = 'index.html';
          } else {
            const errorData = await response.json();
            alert(
              'Login failed: ' + (errorData.message || response.statusText)
            );
          }
        } catch (error) {
          alert('An error occurred while logging in: ' + error.message);
        }
      }

      await loginUser(email, password);
    });
  }

  function checkAuthentication() {
    const token = getCookie('token');
    console.log('token:', token);
    const loginLink = document.getElementById('login-link');

    if (!token || isTokenExpired(token)) {
      loginLink.style.display = 'inline-block';
    } else {
      loginLink.style.display = 'none';
      fetchPlaces(token); // Fetch places data if the user is authenticated
    }
  }

  function getCookie(name) {
    // Function to get a cookie value by its name
    const cookieString = document.cookie;
    const cookies = cookieString.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + '=')) {
        return cookie.substring(name.length + 1);
      }
    }
    return null;
  }

  function isTokenExpired(token) {
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      return payload.exp < Math.floor(Date.now() / 1000);
    } catch (error) {
      console.error('Invalid token:', error);
      return true;
    }
  }

  async function fetchPlaces(token) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/places/`, {
        method: 'GET',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if (!response.ok) {
        throw new Error('Failed to fetch places');
      }
      const data = await response.json();
      displayPlaces(data);
    } catch (error) {
      console.error(error);
      alert('Session expired or invalid token. Please log in again.');
      document.getElementById('login-link').style.display = 'block';
    }
  }

  function displayPlaces(places) {
    const placesContainer = document.getElementById('places-list');
    placesContainer.innerHTML = '';

    places.forEach((place) => {
      const placeElement = document.createElement('div');
      placeElement.className = 'place-card';
      placeElement.innerHTML = `
        <h3>${place.title}</h3>
		<hr>
        <p>${place.description}</p>
		<p>Price: $${place.price} per night</p>
		<p>Latitude: ${place.latitude}</p>
		<p>Longitude: ${place.longitude}</p>
        <button>View Details</button>`;
      placesContainer.appendChild(placeElement);
    });
  }

  // Dropdown Menu
  const dropDownMenu = document.querySelector('#price-filter');

  const array = ['All', '100', '200', '350']
  for (const[index, arr] of array.entries()) {
	const opt = document.createElement('option');
	opt.value = index;
	opt.innerHTML = arr;
	dropDownMenu.appendChild(opt);
  }
});
