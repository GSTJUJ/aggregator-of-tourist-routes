from fastapi import APIRouter
from sqlalchemy import text

from app.database import SessionLocal
from app.schemas.booking import BookingCreate

router = APIRouter()


@router.post("/booking")
def booking(data: BookingCreate):
    db = SessionLocal()

    query = """
    INSERT INTO bookings
    (user_id, tour_id, participants_count, participants_info)
    VALUES
    (:user_id, :tour_id, :participants_count, :participants_info)
    """

    db.execute(
        text(query),
        {
            "user_id": data.user_id,
            "tour_id": data.tour_id,
            "participants_count": data.participants_count,
            "participants_info": data.participants_info
        }
    )

    db.commit()
    db.close()

    return {"message": "Запись создана"}


@router.post("/favorites")
def favorites():
    return {"message": "Добавлено в избранное"}