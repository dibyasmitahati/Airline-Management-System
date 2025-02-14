document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contact-form");

    contactForm.addEventListener("submit", function (event) {
        // Prevent default submission
        event.preventDefault();

        // Simulate form submission
        fetch(contactForm.action, {
            method: contactForm.method,
            body: new FormData(contactForm)
        })
        .then(response => {
            if (response.ok) {
                // Show success message (optional)
                alert("Thank you for your feedback!");

                // Reset the form
                contactForm.reset();
            } else {
                alert("An error occurred. Please try again.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred. Please try again.");
        });
    });
});
