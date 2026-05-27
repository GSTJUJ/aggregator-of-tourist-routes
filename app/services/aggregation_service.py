from sqlalchemy.orm import Session

from app.providers.json_provider import JsonProvider

from app.models.tour import Tour


class AggregationService:

    async def aggregate(
        self,
        db: Session
    ):

        provider = JsonProvider()

        tours = await provider.get_tours()

        added_count = 0

        for item in tours:

            existing_tour = db.query(Tour).filter(
                Tour.external_id == item["id"]
            ).first()

            if existing_tour:
                continue

            new_tour = Tour(

                source="json_provider",

                external_id=item["id"],

                title=item["title"],

                description=item.get("description"),

                city=item.get("city"),

                country=item.get("country"),

                duration=item.get("duration"),

                price=item.get("price"),

                currency=item.get("currency"),

                rating=item.get("rating"),

                image_url=item.get("image_url"),

                source_url=item.get("source_url")
            )

            db.add(new_tour)

            added_count += 1

        db.commit()

        return {
            "message": "Aggregation completed",
            "added_tours": added_count
        }
