function setupProfileButton() {
    const profileButton = document.getElementById("profileButton");

    if (!profileButton) {
        return;
    }

    profileButton.addEventListener("click", () => {
        window.location.href = localStorage.getItem("access_token")
            ? "/profile"
            : "/login-page";
    });
}

setupProfileButton();
