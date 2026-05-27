from app.providers.base_provider import BaseProvider


class JsonProvider(BaseProvider):

    async def get_tours(self):

        return [
            {
                "id": "json_1",

                "title": "Old Riga Walking Tour",

                "description": "Explore the old city.",

                "city": "Riga",

                "country": "Latvia",

                "price": 25,

                "currency": "EUR",

                "duration": "2 hours",

                "rating": 4.7,

                "image_url": "https://example.com/image.jpg",

                "source_url": "https://example.com/tour"
            },

            {
                "id": "json_2",

                "title": "Paris Night Tour",

                "description": "See Paris at night.",

                "city": "Paris",

                "country": "France",

                "price": 40,

                "currency": "EUR",

                "duration": "3 hours",

                "rating": 4.9,

                "image_url": "https://example.com/paris.jpg",

                "source_url": "https://example.com/paris-tour"
            }
        ]
