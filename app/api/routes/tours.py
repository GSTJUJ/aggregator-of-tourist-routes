from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database.database import get_db
from app.schemas.tour import TourResponse
from app.services.tour_service import TourService

router = APIRouter()
tour_service = TourService()


@router.get("/tours", response_model=List[TourResponse])
def get_tours(
    city: Optional[str] = None,
    country: Optional[str] = None,
    max_price: Optional[float] = None,
    limit: int = 10,
    offset: int = 0,
    sort_by: str = "id",
    db: Session = Depends(get_db)
):
    return tour_service.get_all_tours(
        db=db,
        city=city,
        country=country,
        max_price=max_price,
        limit=limit,
        offset=offset,
        sort_by=sort_by
    )


@router.get("/tours/{tour_id}", response_model=TourResponse)
def get_tour_by_id(
    tour_id: int,
    db: Session = Depends(get_db)
):
    return tour_service.get_tour_by_id(
        db=db,
        tour_id=tour_id
    )
