class NormalizationService:

    @staticmethod
    def normalize(data):

        return {
            "external_id": (
                data.get("id")
                or data.get("external_id")
            ),

            "title": (
                data.get("title")
                or data.get("tour_name")
                or data.get("name")
            ),

            "price": (
                data.get("price")
                or data.get("cost")
                or data.get("amount")
            ),
        }
