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

async function loadTours() {
    const params = new URLSearchParams();
    params.set("query", queryInput.value.trim());
    params.set("city", cityInput.value.trim());

    const response = await fetch(`/search?${params.toString()}`);
    const tours = await response.json();

    tourGrid.innerHTML = "";
    resultsCount.textContent = tours.length;
    emptyState.hidden = tours.length > 0;

    tours.forEach((tour) => {
        tourGrid.appendChild(createTourCard(tour));
    });
}

if (searchForm) {
    searchForm.addEventListener("submit", (event) => {
        event.preventDefault();
        loadTours();
    });

    loadTours();
}
