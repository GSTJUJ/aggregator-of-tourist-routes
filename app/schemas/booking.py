from pydantic import BaseModel


class BookingCreate(BaseModel):
    user_id: int
    tour_id: int
    participants_count: int
    participants_info: str