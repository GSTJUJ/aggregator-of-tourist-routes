const excursionsButton = document.getElementById("excursionsButton");

if (excursionsButton) {
    excursionsButton.addEventListener("click", () => {
        window.location.href = "/excursions";
    });
}
