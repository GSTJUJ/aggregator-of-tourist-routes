from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.search_service import SearchService

router = APIRouter()


@router.get("/search")
def search(
    query: str,
    db: Session = Depends(get_db)
):

    return SearchService.search(
        db=db,
        query=query
    )
