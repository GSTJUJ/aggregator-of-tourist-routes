from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.tour import Tour


class SearchService:

    @staticmethod
    def search(
        db: Session,
        query: str = "",
        city: str = ""
    ):
        tours_query = db.query(Tour)

        if query:
            tours_query = tours_query.filter(
                or_(
                    Tour.title.ilike(f"%{query}%"),
                    Tour.description.ilike(f"%{query}%"),
                    Tour.city.ilike(f"%{query}%"),
                    Tour.country.ilike(f"%{query}%")
                )
            )

        if city:
            tours_query = tours_query.filter(
                Tour.city.ilike(f"%{city}%")
            )

        return tours_query.order_by(Tour.rating.desc()).all()
