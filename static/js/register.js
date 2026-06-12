const registerForm = document.getElementById("registerForm");

if (registerForm) {
    registerForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const data = {
            full_name: document.getElementById("full_name").value,
            phone: document.getElementById("phone").value,
            email: document.getElementById("email").value,
            region: document.getElementById("region").value,
            password: document.getElementById("password").value
        };

        const response = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            localStorage.setItem("access_token", result.access_token);
            alert(result.message);
            window.location.href = "/profile";
        } else {
            alert(result.detail || "Ошибка регистрации");
        }
    });
}
