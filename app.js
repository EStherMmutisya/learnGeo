const baseUrl = 'http://localhost:5000/api/data'; // Replace with your API endpoint URL

function fetchData() {
  fetch(baseUrl)
    .then(response => response.json())
    .then(data => {
      // Process and display retrieved data
      console.log(data);
      // Update your UI or DOM elements with the received data
    })
    