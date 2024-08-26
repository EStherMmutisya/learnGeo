const baseUrl = 'http://localhost:5000/api/data'; // Replace with your API endpoint URL

function fetchData() {
  fetch(baseUrl)
    .then(response => response.json())
    .then(data => {
      // Process and display retrieved data
      console.log(data);
      // Update your UI or DOM elements with the received data
    })
    const baseUrl = 'http://localhost:5000/api/data'; // Replace with your API endpoint URL

function fetchData() {
  fetch(baseUrl)
    .then(response => response.json())
    .then(data => {
      // Process and display retrieved data
      console.log(data);
      // Update your UI or DOM elements with the received data
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      // Handle errors gracefully, e.g., display an error message to the user
    });
}


const baseUrl = 'http://localhost:5000/api/data'; // Replace with your API endpoint URL

function fetchData() {
  fetch(baseUrl)
    .then(response => response.json())
    .then(data => {
      // Process and display retrieved data
      console.log(data);
      // Update your UI or DOM elements with the received data
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      // Handle errors gracefully, e.g., display an error message to the user
    });
}

function createData(name) {
  fetch(baseUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name })
 