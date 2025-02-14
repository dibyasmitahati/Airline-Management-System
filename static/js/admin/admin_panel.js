$(document).ready(function () {
    // Highlight active menu item smoothly
    const currentLocation = window.location.href;
    $(".navbar-nav a").each(function () {
        if (this.href === currentLocation) {
            $(this).parent().addClass("active");
        }
    });

    // Smooth hover effects for navbar links
    $(".navbar-nav a").hover(
        function () {
            $(this).css({
                color: "#f0ad4e", // Bootstrap warning color
                transition: "color 0.3s",
            });
        },
        function () {
            $(this).css({
                color: "",
            });
        }
    );

    // Add subtle hover effects for panels
    $(".panel").hover(
        function () {
            $(this).css({
                boxShadow: "0 8px 20px rgba(0, 0, 0, 0.2)", // Soft shadow effect
                transform: "scale(1.02)", // Slight zoom effect
                transition: "all 0.3s ease-in-out",
            });
        },
        function () {
            $(this).css({
                boxShadow: "",
                transform: "",
            });
        }
    );

    // Navbar collapse animation for mobile view
    $(".navbar-toggle").click(function () {
        const isCollapsed = $(".navbar-collapse").hasClass("in");
        $(".navbar-collapse").slideToggle(300).toggleClass("in", !isCollapsed);
    });

    // Animations for page load
    $(".row h1, .row p").css({
        opacity: 0,
        transform: "translateY(30px)",
    });

    $(".row h1").animate(
        {
            opacity: 1,
            transform: "translateY(0)",
        },
        {
            duration: 1000,
            step: function (now, fx) {
                if (fx.prop === "transform") {
                    $(this).css("transform", `translateY(${30 - now}px)`);
                }
            },
        }
    );

    $(".row p").delay(500).animate(
        {
            opacity: 1,
            transform: "translateY(0)",
        },
        {
            duration: 1000,
            step: function (now, fx) {
                if (fx.prop === "transform") {
                    $(this).css("transform", `translateY(${30 - now}px)`);
                }
            },
        }
    );
});
