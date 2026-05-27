from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.aggregation_service import AggregationService


router = APIRouter()


@router.get("/aggregate")
async def aggregate_tours(
    db: Session = Depends(get_db)
):

    service = AggregationService()

    result = await service.aggregate(db)

    return result
