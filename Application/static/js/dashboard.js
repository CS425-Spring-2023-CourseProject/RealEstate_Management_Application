// dashboard.js
document.addEventListener("DOMContentLoaded", function () {
    // Replace the placeholders with the actual user data
    const nameElement = document.querySelector("h2");
    const roleElement = document.querySelector("h3");
  
    nameElement.textContent = `Welcome, ${userName}!`;
    roleElement.textContent = userRole;
  
    const agentContent = document.querySelector(".agent-content");
    const perspectiveRenterContent = document.querySelector(".perspective-renter-content");
  
    // Hide or show content based on the user's role
    switch (userRole) {
      case "Agent":
        agentContent.style.display = "block";
        perspectiveRenterContent.style.display = "none";
        break;
      case "Perspective Renter":
        agentContent.style.display = "none";
        perspectiveRenterContent.style.display = "block";
        break;
    }
  });
  