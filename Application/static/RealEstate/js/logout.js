document.addEventListener("DOMContentLoaded", function () {
  const logoutSection = document.getElementById("logout-section");

  // Send logout request to the backend
  fetch("http://127.0.0.1:8000/api/logout/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value,
    },
  })
    .then((response) => {
      if (response.ok) {
        // Remove any stored session or authentication tokens
        localStorage.removeItem("token");
        sessionStorage.removeItem("token");

        // Show confirmation message
        logoutSection.innerHTML = `
          <h1>You have successfully logged out</h1>
          <p><a href="/login/">Click here</a> to log in again.</p>
        `;
      } else {
        alert("Error logging out. Please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
