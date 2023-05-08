document.getElementById("signup_form").addEventListener("submit", async function (event) {
  event.preventDefault();

  const password = document.getElementById("id_password").value;
  const confirmPassword = document.getElementById("id_confirm_password").value;

  if (password !== confirmPassword) {
    alert("Passwords do not match!");
    return;
  }

  const formData = new FormData(event.target);

  try {
    const response = await fetch("http://127.0.0.1:8000/signup_process/", { // Update this URL to match the Django view handling the form submission
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    });

    if (response.ok) {
      alert("Your registration has been submitted successfully!");
      window.location.href = "http://127.0.0.1:8000/dashboard/"; // Update this URL to the appropriate Django URL for the user dashboard
    } else {
      // Handle server-side validation errors
      const errors = await response.json();
      console.log(errors);
    }
  } catch (error) {
    console.error("Error submitting form:", error);
  }
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
