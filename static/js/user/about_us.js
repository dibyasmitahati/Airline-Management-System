$(document).ready(function () {
    // Smooth Scroll for Internal Links
    $('a').on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate(
                {
                    scrollTop: $(hash).offset().top,
                },
                800,
                function () {
                    window.location.hash = hash;
                }
            );
        }
    });

    // Add Animation to the About Us Section on Page Load
    $('#about-us').css('opacity', 0).animate({ opacity: 1 }, 1500);
});
