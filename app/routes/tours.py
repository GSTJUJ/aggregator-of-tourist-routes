from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Tour

router = APIRouter()


@router.get("/tours")
def get_tours():
    db: Session = SessionLocal()

    tours = db.query(Tour).all()

    result = []

    for tour in tours:
        result.append({
            "tour_id": tour.tour_id,
            "title": tour.title,
            "region": tour.region,
            "price": float(tour.price)
        })

    db.close()

    return result