const loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const data = {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        };

        try {
            const response = await fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                localStorage.setItem("access_token", result.access_token);
                alert("Успешный вход!");
                window.location.href = "/profile";
            } else {
                alert(result.detail || "Ошибка входа");
            }
        } catch (error) {
            alert("Ошибка подключения к серверу");
        }
    });
}
