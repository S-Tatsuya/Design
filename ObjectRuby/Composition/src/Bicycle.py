from abc import ABCMeta, abstractmethod
from src.Parts import Parts, RoadBikeParts


class Bicycle(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        self._size = kwargs.get("size")
        self._parts: Parts = kwargs.get("parts") or RoadBikeParts([])

        self._post_initialize(**kwargs)

    @property
    def size(self):
        return self._size

    @property
    def default_chain(self):
        return "10-speed"

    @property
    def spares(self):
        return self._parts.spares

    @property
    def parts(self):
        return self._parts.parts

    @property
    @abstractmethod
    def default_tire_size(self):
        pass

    @abstractmethod
    def _post_initialize(self, **kwargs):
        pass

    @abstractmethod
    def _local_spares(self) -> dict:
        pass
