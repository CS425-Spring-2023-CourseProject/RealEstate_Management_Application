document.getElementById('booking-form').addEventListener('submit', async function (event) {
    event.preventDefault();
  
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const paymentMethod = document.getElementById('payment-method').value;
    const propertyId = document.getElementById('property-id').value;
  
    const data = {
      start_date: startDate,
      end_date: endDate,
      payment_method: paymentMethod,
      property_id: propertyId,
    };
  
    const response = await fetch('http://127.0.0.1:8000/api/bookings/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // Add your Django CSRF token here
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify(data),
    });
  
    if (response.ok) {
      alert('Booking successful');
      window.location.href = "/dashboard/";
 } else {
      alert('Booking failed. Please try again.');
    }
  });
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }