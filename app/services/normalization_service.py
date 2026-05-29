class NormalizationService:

    @staticmethod
    def normalize(data):

        return {

            "external_id": (
                data.get("id")
                or data.get("external_id")
                or data.get("parser_id")
            ),

            "title": (
                data.get("title")
                or data.get("tour_name")
                or data.get("name")
            ),

            "city": (
                data.get("city")
                or data.get("location_city")
                or data.get("place")
            ),

            "country": (
                data.get("country")
                or data.get("location_country")
                or "Unknown"
            ),

            "price": float(
                data.get("price")
                or data.get("cost")
                or data.get("amount")
                or 0
            ),

            "currency": (
                data.get("currency")
                or data.get("currency_code")
                or data.get("money_type")
                or "RUB"
            ),

            "rating": float(
                data.get("rating")
                or data.get("stars")
                or 0
            ),

            "source": (
                data.get("source")
                or data.get("provider")
                or "unknown"
            )
        }
