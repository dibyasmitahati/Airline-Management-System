document.getElementById('flight-search-form').addEventListener('submit', function (event) {
    event.preventDefault();

    // Retrieve form data
    const from = document.getElementById('from').value.trim();
    const to = document.getElementById('to').value.trim();
    const departureDate = document.getElementById('departure-date').value;

    // Basic validation
    if (!from || !to || !departureDate) {
        alert('Please fill out all fields.');
        return;
    }

    // Fetch flights from the server
    fetch('/user/check-flights', {  // <-- FIXED ROUTE HERE
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            source: from,
            destination: to,
            departure_date: departureDate
        }),
    })
    .then(response => response.json())
    .then(data => {
        const flightResults = document.getElementById('flight-results');
        flightResults.innerHTML = ''; // Clear previous results

        if (data.status === "error") {
            alert(data.message);
            return;
        }

        data.flights.forEach(flight => {
            const flightCard = document.createElement('div');
            flightCard.className = 'flight-card animate__animated animate__fadeIn';
            flightCard.innerHTML = `
                <h4>Flight ID: ${flight.flight_id}</h4>
                <p><strong>From:</strong> ${flight.source}</p>
                <p><strong>To:</strong> ${flight.destination}</p>
                <p><strong>Departure:</strong> ${new Date(flight.departure_time).toLocaleString()}</p>
                <p><strong>Duration:</strong> ${flight.duration}</p>
                <button class="btn btn-success book-ticket" data-id="${flight.flight_id}">
                    Book Ticket
                </button>
            `;
            flightResults.appendChild(flightCard);
        });

        // Add event listeners to book buttons
        document.querySelectorAll('.book-ticket').forEach(button => {
            button.addEventListener('click', function () {
                const flightId = this.getAttribute('data-id');
                window.location.href = `/book-ticket?flight_id=${flightId}`;
            });
        });
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while searching for flights.');
    });
});
