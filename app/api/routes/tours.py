from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from typing import List

from app.database.database import get_db

from app.schemas.tour import TourResponse

from app.services.tour_service import TourService


router = APIRouter()

tour_service = TourService()


@router.get(
    "/tours",
    response_model=List[TourResponse]
)
def get_tours(
    db: Session = Depends(get_db)
):

    return tour_service.get_all_tours(db)
