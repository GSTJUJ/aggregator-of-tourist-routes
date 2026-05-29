from sqlalchemy.orm import Session
from app.models.tour import Tour


class TourService:

    def get_all_tours(
        self,
        db: Session,
        city: str = None,
        country: str = None,
        max_price: float = None,
        limit: int = 10,
        offset: int = 0,
        sort_by: str = "id"
    ):
        query = db.query(Tour)

        # FILTERS
        if city:
            query = query.filter(Tour.city.ilike(f"%{city}%"))
        if country:
            query = query.filter(Tour.country.ilike(f"%{country}%"))
        if max_price:
            query = query.filter(Tour.price <= max_price)

        # SORTING
        if sort_by == "price":
            query = query.order_by(Tour.price)
        elif sort_by == "rating":
            query = query.order_by(Tour.rating.desc())
        else:
            query = query.order_by(Tour.id)

        # PAGINATION
        query = query.offset(offset).limit(limit)

        return query.all()

    def get_tour_by_id(self, db: Session, tour_id: int):
        return db.query(Tour).filter(Tour.id == tour_id).first()
