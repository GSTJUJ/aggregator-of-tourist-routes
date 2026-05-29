from app.providers.json_provider import JsonProvider
from app.providers.xml_provider import XmlProvider


class ProviderManager:

    @staticmethod
    def get_providers():

        return [

            JsonProvider(),

            XmlProvider()
        ]