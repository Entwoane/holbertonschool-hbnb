/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  const API_BASE_URL = 'http://127.0.0.1:3000';
  const loginForm = document.getElementById('login-form');
  let places = [];

  setTimeout(() => {
    checkAuthentication();
  }, 50);

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
    console.log('Token:', token);
    const currentPage = window.location.pathname.split('/').pop();
    const loginLink = document.getElementById('login-link');
    const addReviewSection = document.getElementById('add-review');

    if (currentPage === 'login.html') {
      if (loginLink) loginLink.style.display = 'none';
      return;
    }

    if (!token || isTokenExpired(token)) {
      console.log('Token is missing or expired.');
      document.cookie = 'token=; path=/; max-age=0'; // Clear expired token
      if (loginLink) loginLink.style.display = 'inline-block';
      if (addReviewSection) addReviewSection.style.display = 'none';

      if (currentPage !== 'login.html') {
        alert('Session expired. Please log in again.');
        window.location.href = 'login.html';
      }
    } else {
      console.log('Token is valid.');
      if (loginLink) loginLink.style.display = 'none';
      if (addReviewSection) addReviewSection.style.display = 'inline-block';
      if (currentPage === 'index.html') fetchPlaces(token);

      if (currentPage === 'place.html') {
        const placeId = getPlaceIdFromURL();
        if (placeId) fetchPlaceDetails(token, placeId);
      }
    }
  }

  function getCookie(name) {
    // Function to get a cookie value by its name
    const cookieString = document.cookie;
    const cookies = cookieString.split(';');
    for (let cookie of cookies) {
      const [cookieName, cookieValue] = cookie.trim().split('=');
      if (cookieName === name) return cookieValue;
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

  function displayPlaces(placesToDisplay) {
    const placesContainer = document.getElementById('places-list');
    placesContainer.innerHTML = '';

    if (!placesContainer) {
      console.error('Places container not found!');
      return;
    }

    if (placesToDisplay.length === 0) {
      placesContainer.innerHTML = '<p>No places match your criteria.</p>';
      return;
    }

    placesToDisplay.forEach((place) => {
      const placeElement = document.createElement('div');
      placeElement.className = 'place-card';
      placeElement.innerHTML = `
      <h3>${place.title}</h3>
      <hr>
      <p>${place.description}</p>
      <p>Price: $${place.price} per night</p>
      <p>Latitude: ${place.latitude}</p>
      <p>Longitude: ${place.longitude}</p>
      <button class="view-places-details" data-place-id="${place.id}">View Details</button>`;
      placesContainer.appendChild(placeElement);

      const viewPlacesDetails = placeElement.querySelector(
        '.view-places-details'
      );
      viewPlacesDetails.addEventListener('click', () => {
        window.location.href = `place.html?placeId=${place.id}`;
      });
    });
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
      places = data;
      displayPlaces(data);
    } catch (error) {
      console.error(error);
      document.getElementById('login-link').style.display = 'inline-block';
    }
  }
  function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('placeId');
  }

  async function fetchPlaceDetails(token, placeId) {
    if (!placeId) return;

    try {
      const endpoint = `${API_BASE_URL}/api/v1/places/${placeId}`;
      const headers = {
        Authorization: `Bearer ${token}`,
      };

      const reponse = await fetch(endpoint, { headers });

      if (!reponse.ok) {
        throw new Error(`Error: ${response.status} - ${response.statusText}`);
      }
      const data = await reponse.json();

      displayPlaceDetails(data);
    } catch (error) {
      console.error('Failed to fetch place details:', error);
      const placeDetails = document.getElementById('place-details');
      if (placeDetails) {
        placeDetails.innerHTML =
          '<p>Oops something went wrong. Error while loading details.</p>';
      }
    }
  }

  function displayPlaceDetails(place) {
    const placeDetails = document.getElementById('place-details');
    if (!placeDetails) return;

    placeDetails.innerHTML = `
      <div id="place-name">
        <h1>${place.title}</h1>
      </div>
      <div id="place-description">
        <h4>Host: ${place.owner_first_name} ${place.owner_last_name}</h4>
        <h4>Price per night: $${place.price}</h4>
        <p>Description: ${
          place.description || 'Aucune description disponible'
        }</p>
            <div id="place-amenities">
      <h4>Amenities:</h4>
      <ul id="amenities-list">
        ${
          place.amenities && place.amenities.length > 0
            ? place.amenities
                .map((amenity) => `<li>${amenity.name}</li>`)
                .join('')
            : '<li>No amenities available</li>'
        }
      </ul>
      </div>
    `;
    const reviewsSection = document.getElementById('reviews');
    if (!reviewsSection) return;
    reviewsSection.innerHTML = '<h3>Reviews</h3>';
    if (place.reviews && place.reviews.length > 0) {
      const reviewsList = document.createElement('div');
      reviewsList.className = 'review-cards';
      place.reviews.forEach((review) => {
        const reviewElement = document.createElement('div');
        reviewElement.innerHTML = `
          <h4>User ID: ${review.user_id}</h4>
          <p>${review.text}</p>
        `;
        reviewsList.appendChild(reviewElement);
      });
      reviewsSection.appendChild(reviewsList);
    } else {
      reviewsSection.innerHTML += '<p>No reviews available.</p>';
    }
  }

  // Dropdown Menu
  const dropDownMenu = document.querySelector('#price-filter');
  const priceOptions = ['All', '100', '200', '300'];
  priceOptions.forEach((price) => {
    const option = document.createElement('option');
    option.value = price === 'All' ? 'All' : Number(price);
    option.textContent = price;
    dropDownMenu.appendChild(option);
  });

  dropDownMenu.addEventListener('change', (event) => {
    const selectedPrice = event.target.value;

    let filteredPlaces;
    if (selectedPrice === 'All') {
      filteredPlaces = places;
    } else {
      filteredPlaces = places.filter(
        (place) => place.price <= Number(selectedPrice)
      );
    }
    displayPlaces(filteredPlaces);
  });
});
