$(document).ready(function() {
    $('#loginForm').on('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        // Perform validation
        const email = $('#email').val();
        const password = $('#password').val();

        if (!email || !password) {
            alert('Please fill in all fields.');
            return;
        }

        // Simulate a login request (replace with actual AJAX call)
        console.log('Logging in with:', email, password);

        // Redirect or show success message (replace with actual logic)
        alert('Login successful!');
        // window.location.href = '/dashboard'; // Redirect to dashboard
    });
});