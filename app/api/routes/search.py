from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database.database import get_db

from app.schemas.tour import TourResponse
from app.services.search_service import SearchService

router = APIRouter()


@router.get("/search", response_model=List[TourResponse])
def search(
    query: Optional[str] = "",
    city: Optional[str] = "",
    db: Session = Depends(get_db)
):

    return SearchService.search(
        db=db,
        query=query or "",
        city=city or ""
    )
