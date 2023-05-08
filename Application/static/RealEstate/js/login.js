document.querySelector("form").addEventListener("submit", function (event) {
    event.preventDefault();
  
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    if (validateEmail(email) && validatePassword(password)) {
      // Send the data to the backend using an AJAX request
      sendLoginRequest(email, password);
    } else {
      alert("Please enter a valid email and password.");
    }
  });
  
  function validateEmail(email) {
    const regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    return regex.test(email);
  }
  
  function validatePassword(password) {
    return password.length >= 6;
  }
  
  function sendLoginRequest(email, password) {
    fetch("http://127.0.0.1:8000/api/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value,
      },
      body: `email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert(data.message);
          // Redirect to the home page or any other page after successful login
          window.location.href = "/dashboard.html";
        } else {
          alert(data.message);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  