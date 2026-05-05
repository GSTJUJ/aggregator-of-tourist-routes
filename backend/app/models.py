from sqlalchemy import Column, Integer, Text, Date, Numeric
from app.database import Base

class Tour(Base):
    __tablename__ = "tours"

    tour_id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    region = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    price = Column(Numeric)
    description = Column(Text)
    duration = Column(Text)