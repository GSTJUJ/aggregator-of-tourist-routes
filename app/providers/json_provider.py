import json
from pathlib import Path

from app.providers.base_provider import BaseProvider


class JsonProvider(BaseProvider):

    async def get_tours(self):

        json_path = Path("app/data/provider1.json")

        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            item["source"] = "json_provider"

        return data

