from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(255), nullable=False)

    phone = Column(String(50), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    region = Column(String(255), nullable=False)

    password = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
