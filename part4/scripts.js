/* 
This is a SAMPLE FILE to get you started.
Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  const API_BASE_URL = 'http://127.0.0.1:3000';
  const loginForm = document.getElementById('login-form');
  const reviewForm = document.getElementById('review-form');
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

  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const token = getCookie('token');
      if (!token || isTokenExpired(token)) {
        alert('You need to be logged in to add a review.');
        window.location.href = 'login.html';
        return;
      }

      const reviewText = document.getElementById('review-text').value;
      placeId = getPlaceIdFromURL();

      if (!placeId || !reviewText.trim()) {
        alert('Please provide valid review text.');
        return;
      }

      try {
        submitReview(token, placeId, reviewText);
      } catch (error) {
        console.error(error);
        alert('An error occurred while submitting your review');
      }
      await submitReview(token, placeId, reviewText, reviewForm);
    });
  }

  async function submitReview(token, placeId, reviewText) {
    try {
      const response = await fetch(
        `${API_BASE_URL}/api/v1/places/${placeId}/reviews/`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({ text: reviewText }),
        }
      );

      handleResponse(response, reviewForm);
    } catch (error) {
      console.error(error);
      alert('An error occurred while submitting your review');
    }
  }

  function handleResponse(response, reviewForm) {
    if (response.ok) {
      alert('Review submitted successfully!');
      window.location.href = `place.html?placeId=${getPlaceIdFromURL}`;
    } else {
      alert('Failed to submit review');
    }
  }

  function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('placeId');
  }

  function checkAuthentication() {
    const token = getCookie('token');
    console.log('Token:', token);
    const currentPage = window.location.pathname.split('/').pop();
    const loginLink = document.getElementById('login-link');
    const addReviewSection = document.getElementById('add-review');
    const addReviewButton = document.getElementById('add-review-button');
    const authRequiredPages = ['add_review.html'];

    if (currentPage === 'login.html') {
      if (loginLink) loginLink.style.display = 'none';
      return;
    }

    if (!token || isTokenExpired(token)) {
      console.log('Token is missing or expired.');
      document.cookie = 'token=; path=/; max-age=0'; // Clear expired token
      if (loginLink) loginLink.style.display = 'inline-block';
      if (addReviewSection) addReviewSection.style.display = 'none';
      if (addReviewButton) addReviewButton.style.display = 'none';

      if (authRequiredPages.includes(currentPage)) {
        alert('Session expired. Please log in again.');
        window.location.href = 'login.html';
      }
    } else {
      console.log('Token is valid.');
      if (loginLink) loginLink.style.display = 'none';
      if (addReviewSection) addReviewSection.style.display = 'flex';
      if (addReviewButton) addReviewButton.style.display = 'block';
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

    const existingCards = Array.from(placesContainer.children);
    existingCards.forEach((card) => {
      card.classList.add('disappear');
      setTimeout(() => {
        card.remove();
      }, 500);
    });

    setTimeout(() => {
      placesToDisplay.forEach((place, index) => {
        const placeElement = document.createElement('div');
        placeElement.className = 'place-card';
        placeElement.innerHTML = `
          <h3>${place.title}</h3>
          <hr>
          <p>${place.description}</p>
          <div class="pc-price">
          <p>Price: $${place.price} per night</p>
          <button class="view-places-details" data-place-id="${place.id}">View Details</button>
          </div>`;

        placesContainer.appendChild(placeElement);

        setTimeout(() => {
          placeElement.classList.add('animate');
        }, index * 100);

        const viewPlacesDetails = placeElement.querySelector(
          '.view-places-details'
        );
        viewPlacesDetails.addEventListener('click', () => {
          window.location.href = `place.html?placeId=${place.id}`;
        });
      });
    }, 500);
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
      <hr>
      <div id="place-description">
        <h4>Host: ${place.owner_first_name} ${place.owner_last_name}</h4>
        <p>${place.description || 'No description available'}</p>
        <div id="price-per-night">
          <h4>Price per night: $${place.price}</h4>
        </div>
            <div id="place-amenities">
      <h4>Amenities:</h4>
      <ul id="amenities-list">
        ${
          place.amenities && place.amenities.length > 0
            ? place.amenities
                .map((amenity) => `<li>&#10004; ${amenity.name}</li>`)
                .join('')
            : '<li>No amenities available</li>'
        }
      </ul>
      </div>
      <div id="location">
        <h4>Location:</h4>
        <p>Latitude: ${place.latitude} <br>
        Longitude: ${place.longitude}
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
    const addReviewButton = document.createElement('button');
    addReviewButton.id = 'add-review-button';
    addReviewButton.textContent = 'Add Review';
    addReviewButton.onclick = () => {
      window.location.href = `add_review.html?placeId=${place.id}`;
    };
    reviewsSection.appendChild(addReviewButton);
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
