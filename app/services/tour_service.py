from sqlalchemy.orm import Session

from app.models.tour import Tour


class TourService:

    def get_all_tours(
        self,
        db: Session
    ):

        return db.query(Tour).all()
