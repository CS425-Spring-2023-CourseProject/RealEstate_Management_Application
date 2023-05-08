// Get the forms and add event listeners
const personalDetailsForm = document.getElementById('personal-details-form');
personalDetailsForm.addEventListener('submit', updatePersonalDetails);

const preferredNeighborhoodsForm = document.getElementById('preferred-neighborhoods-form');
preferredNeighborhoodsForm.addEventListener('submit', updatePreferredNeighborhoods);

const creditCardForms = document.getElementsByClassName('credit-card-form');
for (let i = 0; i < creditCardForms.length; i++) {
  creditCardForms[i].addEventListener('submit', updateCreditCard);
}

// Function to send a PATCH request to the API to update personal details
async function updatePersonalDetails(event) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  try {
    const response = await fetch(form.action, {
      method: 'PATCH',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: formData,
    });

    if (response.ok) {
      alert('Personal details updated successfully');
    } else {
      alert('Failed to update personal details');
    }
  } catch (error) {
    console.error(error);
    alert('An error occurred while updating personal details');
  }
}

// Function to send a PATCH request to the API to update preferred neighborhoods
async function updatePreferredNeighborhoods(event) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  try {
    const response = await fetch(form.action, {
      method: 'PATCH',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: formData,
    });

    if (response.ok) {
      alert('Preferred neighborhoods updated successfully');
    } else {
      alert('Failed to update preferred neighborhoods');
    }
  } catch (error) {
    console.error(error);
    alert('An error occurred while updating preferred neighborhoods');
  }
}

// Function to send a PATCH request to the API to update credit card information
async function updateCreditCard(event) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  try {
    const response = await fetch(form.action, {
      method: 'PATCH',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: formData,
    });

    if (response.ok) {
      alert('Credit card information updated successfully');
    } else {
      alert('Failed to update credit card information');
    }
  } catch (error) {
    console.error(error);
    alert('An error occurred while updating credit card information');
  }
}

// Function to get the CSRF token from cookies
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}
