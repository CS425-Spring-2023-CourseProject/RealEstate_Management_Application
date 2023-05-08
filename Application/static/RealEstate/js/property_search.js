document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.getElementById("search-form");
  const searchResults = document.getElementById("search-results");

  searchForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const location = document.getElementById("location").value;
    const date = document.getElementById("date").value;
    const property_type = document.getElementById("property_type").value;
    const price_range = document.getElementById("price_range").value;

    const response = await fetch("/property_search/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({
        location: location,
        date: date,
        property_type: property_type,
        price_range: price_range,
      }),
    });

    const properties = await response.json();
    displayProperties(properties);
  });

  function displayProperties(properties) {
    searchResults.innerHTML = "";

    if (properties.length === 0) {
      searchResults.innerHTML = "<p>No properties found.</p>";
      return;
    }

    properties.forEach((property) => {
      const propertyElement = document.createElement("div");
      propertyElement.className = "property";
      propertyElement.innerHTML = `
          <h3>${property.fields.address}</h3>
          <p>Property type: ${property.fields.property_type}</p>
          <p>Price: ${property.fields.price}</p>
          <p>Date available: ${property.fields.date_available}</p>
      `;
      searchResults.appendChild(propertyElement);
    });
  }

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
  }
  
});
