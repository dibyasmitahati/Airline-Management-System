document.addEventListener('DOMContentLoaded', function () {
    console.log('Staff Management JS loaded.');

    // Add form validation for adding staff
    const addStaffForm = document.getElementById('add-staff-form');
    addStaffForm.addEventListener('submit', function (event) {
        const name = addStaffForm.querySelector('input[name="name"]').value.trim();
        const email = addStaffForm.querySelector('input[name="email"]').value.trim();

        if (!name || !email) {
            event.preventDefault();
            alert('Please fill out all required fields.');
        }
    });

    // Smooth scroll for in-page navigation
    const navLinks = document.querySelectorAll('.navbar-nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            if (this.hash !== '') {
                event.preventDefault();
                const target = document.querySelector(this.hash);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // Add animation on table row hover
    const staffRows = document.querySelectorAll('.table tbody tr');
    staffRows.forEach(row => {
        row.addEventListener('mouseenter', function () {
            this.style.backgroundColor = '#f0f8ff';
        });
        row.addEventListener('mouseleave', function () {
            this.style.backgroundColor = '';
        });
    });

    // Confirmation popup for removing staff
    const removeButtons = document.querySelectorAll('form[action="{{ url_for("remove_staff") }}"] button');
    removeButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            if (!confirm('Are you sure you want to remove this staff member?')) {
                event.preventDefault();
            }
        });
    });
});
