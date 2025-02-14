document.getElementById('flight-search-form').addEventListener('submit', function (event) {
    event.preventDefault();

    // Retrieve form data
    const from = document.getElementById('from').value.trim();
    const to = document.getElementById('to').value.trim();
    const departureDate = document.getElementById('departure-date').value;
    const flightClass = document.getElementById('class').value;

    // Basic validation
    if (!from || !to || !departureDate || !flightClass) {
        alert('Please fill out all fields.');
        return;
    }

    // Fetch flights from the server
    fetch('/search-flights', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            source: from,
            destination: to,
            departure_date: departureDate,
        }),
    })
    .then(response => response.json())
    .then(data => {
        const flightResults = document.getElementById('flight-results');
        flightResults.innerHTML = ''; // Clear previous results

        if (data.length > 0) {
            data.forEach(flight => {
                const flightCard = document.createElement('div');
                flightCard.className = 'flight-card animate__animated animate__fadeIn';
                flightCard.innerHTML = `
                    <h4>Flight ID: ${flight.flight_id}</h4>
                    <p><strong>From:</strong> ${flight.source}</p>
                    <p><strong>To:</strong> ${flight.destination}</p>
                    <p><strong>Departure:</strong> ${new Date(flight.departure_time).toLocaleString()}</p>
                    <p><strong>Duration:</strong> ${flight.duration}</p>
                `;
                flightResults.appendChild(flightCard);
            });
        } else {
            const noFlights = document.createElement('div');
            noFlights.className = 'no-flights animate__animated animate__fadeIn';
            noFlights.textContent = 'No flights available for the selected route and date.';
            flightResults.appendChild(noFlights);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while searching for flights.');
    });
});