from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.tour import Tour


class SearchService:

    @staticmethod
    def search(
        db: Session,
        query: str
    ):

        return db.query(Tour).filter(

            or_(

                Tour.title.ilike(f"%{query}%"),

                Tour.city.ilike(f"%{query}%"),

                Tour.country.ilike(f"%{query}%")
            )

        ).all()
