from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)

from datetime import datetime

from app.database.database import Base


class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    tour_id = Column(
        Integer,
        ForeignKey("tours.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
