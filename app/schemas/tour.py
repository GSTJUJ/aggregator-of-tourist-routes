from pydantic import BaseModel
from typing import Optional


class TourResponse(BaseModel):

    id: int

    title: str

    description: Optional[str]

    city: Optional[str]

    country: Optional[str]

    price: Optional[float]

    currency: Optional[str]

    duration: Optional[str]

    rating: Optional[float]

    image_url: Optional[str]

    source: Optional[str]

    source_url: Optional[str]


    class Config:
        from_attributes = True
