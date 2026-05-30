from pathlib import Path
from bs4 import BeautifulSoup

from app.providers.base_provider import BaseProvider


class ParserProvider(BaseProvider):

    async def get_tours(self):

        html_path = Path("app/data/provider3.html")

        with open(html_path, encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        tours = []

        for index, card in enumerate(soup.select(".tour-card"), start=1):

            tours.append({
                "external_id": f"parser_{index}",
                "name": card.select_one(".name").text,
                "amount": float(card.select_one(".amount").text),
                "place": card.select_one(".place").text,
                "provider": "parser_provider"
            })

        return tours
