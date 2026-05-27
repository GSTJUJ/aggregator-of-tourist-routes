import json

from app.providers.base import BaseProvider


class JsonProvider(BaseProvider):

    async def get_tours(self):

        with open("app/data/provider1.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return data
