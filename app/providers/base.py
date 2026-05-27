from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    async def get_tours(self):
        pass
