$(document).ready(function() {
    $('#registerForm').on('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        // Perform validation
        const name = $('#name').val();
        const surname = $('#surname').val();
        const gender = $('#gender').val();
        const dob = $('#dob').val();
        const email = $('#email').val();
        const phone = $('#phone').val();
        const street = $('#street').val();
        const locality = $('#locality').val();
        const city = $('#city').val();
        const country = $('#country').val();
        const password = $('#password').val();
        const language = $('#language').val();
        const nationality = $('#nationality').val();

        if (!name || !surname || !gender || !dob || !email || !phone || !street || !locality || !city || !country || !password || !language || !nationality) {
            alert('Please fill in all fields.');
            return;
        }

        // Submit the form data to the server
        $.ajax({
            url: '/user/register',
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                // Redirect to the login page on success
                window.location.href = '/user/login';
            },
            error: function(xhr, status, error) {
                alert('Registration failed. Please try again.');
            }
        });
    });
});