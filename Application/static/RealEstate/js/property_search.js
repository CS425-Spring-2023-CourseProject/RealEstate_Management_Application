document.addEventListener("DOMContentLoaded", () => {
    const searchForm = document.querySelector(".search-properties form");
  
    searchForm.addEventListener("submit", async (event) => {
      event.preventDefault();
  
      const location = document.getElementById("location").value;
      const date = document.getElementById("date").value;
      const propertyType = document.getElementById("property-type").value;
      const priceRange = document.getElementById("price-range").value;
  
      const searchParams = {
        location,
        date,
        property_type: propertyType,
        price_range: priceRange,
      };
  
      const response = await fetch("/property_search/", {
        method: "POST",
        body: JSON.stringify(searchParams),
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
      });
  
      const properties = await response.json();
      displayProperties(properties);
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
  
    function displayProperties(properties) {
      const propertyResults = document.querySelector(".property-results");
      propertyResults.innerHTML = "";
  
      if (properties.length === 0) {
        const noResultsMessage = document.createElement("p");
        noResultsMessage.textContent = "No properties found.";
        propertyResults.appendChild(noResultsMessage);
      } else {
        properties.forEach((property) => {
          const propertyElement = document.createElement("div");
          propertyElement.classList.add("property");
  
          // Display property details
          // Example: propertyElement.innerHTML = `<h3>${property.fields.address}</h3>`;
  
          propertyResults.appendChild(propertyElement);
        });
      }
    }
  });
  