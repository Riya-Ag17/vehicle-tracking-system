// Initialize the map
var map = L.map('map').setView([13.0827, 80.2707], 13);

// Add OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Add a marker for the vehicle
var vehicleMarker = L.marker([13.0827, 80.2707]).addTo(map)
    .bindPopup('Vehicle Location')
    .openPopup();

// Function to update position from backend
function updateVehiclePosition() {
    fetch('/get_location')
        .then(response => response.json())
        .then(data => {
            let lat = data.lat;
            let lng = data.lng;
            vehicleMarker.setLatLng([lat, lng]);
            map.setView([lat, lng], map.getZoom());
        })
        .catch(err => console.error('Error fetching location:', err));
}

// Update every 3 seconds
setInterval(updateVehiclePosition, 3000);
