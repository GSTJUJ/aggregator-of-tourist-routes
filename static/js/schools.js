const searchForm = document.getElementById("searchForm");
const queryInput = document.getElementById("queryInput");
const cityInput = document.getElementById("cityInput");
const tourGrid = document.getElementById("tourGrid");
const emptyState = document.getElementById("emptyState");
const resultsCount = document.getElementById("resultsCount");
function formatPrice(tour) {
    if (!tour.price) {
        return "Цена уточняется";
    }

    return `${Number(tour.price).toLocaleString("ru-RU")} ${tour.currency || "RUB"}`;
}

function matchesExtraQuery(tour, query) {
    if (!query) {
        return true;
    }

    const text = [
        tour.title,
        tour.description,
        tour.city,
        tour.country
    ].join(" ").toLowerCase();

    return text.includes(query.toLowerCase());
}

function isSchoolTour(tour) {
    const text = [
        tour.title,
        tour.description,
        tour.city,
        tour.country
    ].join(" ").toLowerCase();

    const schoolWords = [
        "школь",
        "учен",
        "класс",
        "педагог",
        "профориентац",
        "наукоград",
        "музей",
        "мастер-класс"
    ];
    const adultWords = ["взросл"];

    return schoolWords.some((word) => text.includes(word))
        && !adultWords.some((word) => text.includes(word));
}

function createTourCard(tour) {
    const card = document.createElement("article");
    card.className = "tour-card";

    card.innerHTML = `
      <div class="tour-image">
        ${tour.image_url ? `<img src="${tour.image_url}" alt="">` : `<span>${tour.city || "Экскурсия"}</span>`}
      </div>
      <div class="tour-card-body">
        <div class="tour-meta">
          <span>${tour.city || "Город не указан"}</span>
          <span>${tour.rating ? `★ ${tour.rating}` : "Без рейтинга"}</span>
        </div>
        <h3>${tour.title}</h3>
        <p>${tour.description || "Описание скоро появится"}</p>
        <div class="tour-footer">
          <strong>${formatPrice(tour)}</strong>
        </div>
      </div>
    `;

    return card;
}

async function loadSchoolTours() {
    const params = new URLSearchParams();
    params.set("query", "");
    params.set("city", cityInput.value.trim());

    const response = await fetch(`/search?${params.toString()}`);
    const tours = await response.json();
    const filteredTours = tours.filter((tour) => {
        return isSchoolTour(tour)
            && matchesExtraQuery(tour, queryInput.value.trim());
    });

    tourGrid.innerHTML = "";
    resultsCount.textContent = filteredTours.length;
    emptyState.hidden = filteredTours.length > 0;

    filteredTours.forEach((tour) => {
        tourGrid.appendChild(createTourCard(tour));
    });
}

if (searchForm) {
    searchForm.addEventListener("submit", (event) => {
        event.preventDefault();
        loadSchoolTours();
    });

    loadSchoolTours();
}
