const token = localStorage.getItem("access_token");

if (!token) {
    window.location.href = "/login-page";
}

document.getElementById("logoutButton").addEventListener("click", () => {
    localStorage.removeItem("access_token");
    window.location.href = "/";
});

const avatarImage = document.getElementById("avatarImage");
const avatarInput = document.getElementById("avatarInput");
const savedAvatar = localStorage.getItem("profile_avatar");
const mainProfileLink = document.getElementById("mainProfileLink");
const settingsProfileLink = document.getElementById("settingsProfileLink");
const settingsCard = document.getElementById("settingsCard");
const profileSettingsForm = document.getElementById("profileSettingsForm");
const settingsFullName = document.getElementById("settingsFullName");
const settingsEmail = document.getElementById("settingsEmail");
const settingsRegion = document.getElementById("settingsRegion");
const settingsPhone = document.getElementById("settingsPhone");

function showMainProfile(event) {
    event.preventDefault();
    settingsCard.hidden = true;
    mainProfileLink.classList.add("active");
    settingsProfileLink.classList.remove("active");
}

function showSettings(event) {
    event.preventDefault();
    settingsCard.hidden = false;
    settingsProfileLink.classList.add("active");
    mainProfileLink.classList.remove("active");
}

mainProfileLink.addEventListener("click", showMainProfile);
settingsProfileLink.addEventListener("click", showSettings);

if (savedAvatar) {
    avatarImage.src = savedAvatar;
}

document.getElementById("avatarEditButton").addEventListener("click", () => {
    avatarInput.click();
});

avatarInput.addEventListener("change", () => {
    const file = avatarInput.files[0];

    if (!file) {
        return;
    }

    const reader = new FileReader();

    reader.addEventListener("load", () => {
        localStorage.setItem("profile_avatar", reader.result);
        avatarImage.src = reader.result;
    });

    reader.readAsDataURL(file);
});

async function loadProfile() {
    const response = await fetch("/me", {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (!response.ok) {
        localStorage.removeItem("access_token");
        window.location.href = "/login-page";
        return;
    }

    const user = await response.json();
    document.getElementById("profileFullName").textContent = user.full_name;
    document.getElementById("infoFullName").textContent = user.full_name;
    document.getElementById("infoRegion").textContent = user.region;
    document.getElementById("infoEmail").textContent = user.email;
    document.getElementById("infoPhone").textContent = user.phone;
    document.getElementById("infoId").textContent = user.id;

    settingsFullName.value = user.full_name;
    settingsEmail.value = user.email;
    settingsRegion.value = user.region;
    settingsPhone.value = user.phone;
}

profileSettingsForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const response = await fetch("/me", {
        method: "PUT",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            full_name: settingsFullName.value.trim(),
            email: settingsEmail.value.trim(),
            region: settingsRegion.value.trim(),
            phone: settingsPhone.value.trim()
        })
    });

    const result = await response.json();

    if (!response.ok) {
        alert(result.detail || "Не удалось сохранить профиль");
        return;
    }

    document.getElementById("profileFullName").textContent = result.full_name;
    document.getElementById("infoFullName").textContent = result.full_name;
    document.getElementById("infoRegion").textContent = result.region;
    document.getElementById("infoEmail").textContent = result.email;
    document.getElementById("infoPhone").textContent = result.phone;

    alert(result.message || "Профиль обновлен");
    showMainProfile(event);
});

loadProfile();
