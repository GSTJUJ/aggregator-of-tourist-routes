from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    Numeric,
    DateTime
)

from datetime import datetime

from app.database.database import Base


class Tour(Base):

    __tablename__ = "tours"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(String(100), nullable=False)

    external_id = Column(String(255))

    title = Column(String(255), nullable=False)

    description = Column(Text)

    city = Column(String(100))

    country = Column(String(100))

    duration = Column(String(100))

    price = Column(Numeric(10, 2))

    currency = Column(String(10), default="EUR")

    rating = Column(Float)

    image_url = Column(Text)

    source_url = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
