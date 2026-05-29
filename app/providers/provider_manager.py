from app.providers.json_provider import JsonProvider
from app.providers.xml_provider import XmlProvider
from app.providers.parser_provider import ParserProvider


class ProviderManager:

    @staticmethod
    def get_providers():

        return [
            JsonProvider(),
            XmlProvider(),
            ParserProvider()
        ]
