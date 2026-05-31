import xml.etree.ElementTree as ET
from pathlib import Path

from app.providers.base_provider import BaseProvider


class XmlProvider(BaseProvider):

    async def get_tours(self):

        xml_path = Path("app/data/provider2.xml")

        tree = ET.parse(xml_path)
        root = tree.getroot()

        tours = []

        for item in root.findall("tour"):

            tours.append({
         "external_id": item.findtext("external_id"),
         "tour_name": item.findtext("tour_name"),
         "location_city": item.findtext("location_city"),
         "location_country": item.findtext("location_country"),
         "cost": float(item.findtext("cost")),
         "stars": float(item.findtext("stars")),
         "description": item.findtext("description"),
         "duration": item.findtext("duration"),
         "image_url": item.findtext("image_url"),
         "provider": "xml_provider"
        })

        return tours
