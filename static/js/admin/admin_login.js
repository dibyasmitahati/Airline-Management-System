// Handle form animations or additional interactivity
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector(".login-form");
    const messageContainer = document.getElementById("message-container");

    loginForm.addEventListener("submit", (event) => {
        const passwordInput = document.getElementById("password");
        if (!passwordInput.value) {
            event.preventDefault();
            showMessage("Password cannot be empty!", "danger");
        }
    });

    function showMessage(message, type) {
        messageContainer.innerHTML = `
            <div class="alert alert-${type}">${message}</div>
        `;
        setTimeout(() => {
            messageContainer.innerHTML = "";
        }, 3000);
    }
});
