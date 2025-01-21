$(document).ready(function () {
    // Highlight active menu item
    const currentLocation = window.location.href;
    $(".navbar-nav a").each(function () {
        if (this.href === currentLocation) {
            $(this).parent().addClass("active");
        }
    });

    // Show a welcome toast (Example)
    setTimeout(() => {
        alert("Welcome to the Airline-Z Admin Panel!");
    }, 500);
});
