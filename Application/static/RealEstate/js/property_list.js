document.addEventListener("DOMContentLoaded", () => {
    const sortBySelect = document.getElementById("sort-by");
    let properties;
  
    async function fetchProperties() {
      const response = await fetch("property_list/");
      properties = await response.json();
      displayProperties(properties);
    }
  
    function displayProperties(properties) {
      const propertyResults = document.querySelector(".property-results");
      propertyResults.innerHTML = "";
  
      properties.forEach((property) => {
        const propertyElement = document.createElement("li");
        
        // Display property details
        // Example: propertyElement.innerHTML = `<h3>${property.fields.address}</h3>`;
        
        propertyResults.appendChild(propertyElement);
      });
    }
  
    function sortProperties(criteria) {
      if (criteria === "price") {
        properties.sort((a, b) => a.fields.price - b.fields.price);
      } else if (criteria === "bedrooms") {
        properties.sort((a, b) => a.fields.bedrooms - b.fields.bedrooms);
      }
  
      displayProperties(properties);
    }
  
    sortBySelect.addEventListener("change", (event) => {
      sortProperties(event.target.value);
    });
  
    fetchProperties();
  });
  