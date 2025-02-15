document.getElementById('cancel-ticket-form').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent the default form submission

    const ticketId = document.getElementById('ticket-id').value;

    if (!ticketId) {
        alert('Please enter a valid Ticket ID.');
        return;
    }

    fetch('/user/cancel-ticket', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ticket_id: ticketId }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            alert('Ticket canceled successfully! A refund has been initiated.');
            document.getElementById('cancel-ticket-form').reset();
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while canceling the ticket.');
    });
});