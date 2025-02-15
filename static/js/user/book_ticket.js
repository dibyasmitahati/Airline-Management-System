document.addEventListener('DOMContentLoaded', function () {
    // Extract flight_id from URL
    const urlParams = new URLSearchParams(window.location.search);
    const flightId = urlParams.get('flight_id');

    if (flightId) {
        document.getElementById('flight_id').value = flightId;
    } else {
        alert('No flight selected. Please go back and select a flight.');
        window.location.href = '/check-flights'; // Redirect to flight search page
    }
});

document.getElementById('book-ticket-form').addEventListener('submit', function (event) {
    event.preventDefault();

    // Collect form data
    const formData = {
        flight_id: document.getElementById('flight_id').value,
        salutation: document.getElementById('salutation').value,
        first_name: document.getElementById('first_name').value,
        last_name: document.getElementById('last_name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        child_first_name: document.getElementById('child_first_name').value,
        child_last_name: document.getElementById('child_last_name').value,
        dob: document.getElementById('dob').value,
        fare: document.getElementById('fare').value,
        card_number: document.getElementById('card_number').value,
        expiry_date: document.getElementById('expiry_date').value,
        cvv: document.getElementById('cvv').value,
    };

    // Simulate payment processing
    alert('Processing payment...');

    // Send data to the server
    fetch('/process-booking', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            alert('Payment successful! Your ticket has been booked.');
            window.location.href = `/view-ticket?ticket_id=${data.ticket_id}`; // Redirect to view ticket page
        } else {
            alert('Payment failed. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing your payment.');
    });
});