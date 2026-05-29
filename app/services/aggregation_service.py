from sqlalchemy.orm import Session

from app.models.tour import Tour

from app.providers.provider_manager import ProviderManager

from app.services.normalization_service import NormalizationService


class AggregationService:

    async def aggregate(
        self,
        db: Session
    ):

        providers = ProviderManager.get_providers()

        added_count = 0

        for provider in providers:

            tours = await provider.get_tours()

            for raw_item in tours:

                item = NormalizationService.normalize(raw_item)

                existing_tour = db.query(Tour).filter(
                    Tour.external_id == item["external_id"]
                ).first()

                if existing_tour:
                    continue

                new_tour = Tour(

                    source=item["source"],

                    external_id=item["external_id"],

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
