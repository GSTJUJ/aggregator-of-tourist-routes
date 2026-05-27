from app.providers.base_provider import BaseProvider

import xml.etree.ElementTree as ET


class XmlProvider(BaseProvider):

    async def get_tours(self):

        xml_data = """
        <tours>

            <tour>
                <id>xml_1</id>

                <title>Rome экскурсия</title>

                <description>Ancient Rome tour</description>

                <city>Rome</city>

                <country>Italy</country>

                <price>55</price>

                <currency>EUR</currency>

                <duration>4 hours</duration>

                <rating>4.8</rating>

                <image_url>https://example.com/rome.jpg</image_url>

                <source_url>https://example.com/rome-tour</source_url>
            </tour>

        </tours>
        """

        root = ET.fromstring(xml_data)

        tours = []

        for tour in root.findall("tour"):

            tours.append({

                "id": tour.find("id").text,

                "title": tour.find("title").text,

                "description": tour.find("description").text,

                "city": tour.find("city").text,

                "country": tour.find("country").text,

                "price": float(tour.find("price").text),

                "currency": tour.find("currency").text,

                "duration": tour.find("duration").text,

                "rating": float(tour.find("rating").text),

                "image_url": tour.find("image_url").text,

                "source_url": tour.find("source_url").text
            })

        return tours
