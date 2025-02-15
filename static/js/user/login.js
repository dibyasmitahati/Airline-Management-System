$(document).ready(function() {
    $('#loginForm').on('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const email = $('#email').val();
        const password = $('#password').val();

        if (!email || !password) {
            alert('Please fill in all fields.');
            return;
        }

        $.ajax({
            url: '/user/login',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ email: email, password: password }),
            success: function(response) {
                alert(response.message);
                if (response.status === "success") {
                    window.location.href = "/user/user-panel"; // Redirect to user panel
                }
            },
            error: function(xhr) {
                const errorMsg = xhr.responseJSON ? xhr.responseJSON.message : "Login failed";
                alert(errorMsg);
            }
        });
    });
});
