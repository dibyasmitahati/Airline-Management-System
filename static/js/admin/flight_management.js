document.addEventListener('DOMContentLoaded', function () {
    const addFlightForm = document.getElementById('add-flight-form');
    const removeFlightForm = document.getElementById('remove-flight-form');
    const modifyFlightForm = document.getElementById('modify-flight-form');
    const searchFlightForm = document.getElementById('search-flight-form');

    // Add Flight
    addFlightForm.addEventListener('submit', function (event) {
        event.preventDefault();
        alert("Flight added successfully!");
        this.submit(); // Continue to the server
    });

    // Remove Flight
    removeFlightForm.addEventListener('submit', function (event) {
        event.preventDefault();
        if (confirm("Are you sure you want to remove this flight?")) {
            alert("Flight removed successfully!");
            this.submit(); // Continue to the server
        }
    });

    // Modify Flight
    modifyFlightForm.addEventListener('submit', function (event) {
        event.preventDefault();
        alert("Flight modified successfully!");
        this.submit(); // Continue to the server
    });

    // Search Flight
    searchFlightForm.addEventListener('submit', function (event) {
        event.preventDefault();
        alert("Searching for the flight...");
        this.submit(); // Continue to the server
    });
});
