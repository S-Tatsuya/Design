from abc import ABCMeta, abstractmethod


class Bicycle(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        self._size = kwargs.get("size")
        self._chain = kwargs.get("chain") or self.default_chain
        self._tire_size = kwargs.get("tire_size") or self.default_tire_size

    @property
    def size(self):
        return self._size

    @property
    def tire_size(self):
        return self._tire_size

    @property
    def chain(self):
        return self._chain

    @property
    def default_chain(self):
        return "10-speed"

    @property
    @abstractmethod
    def default_tire_size(self):
        pass

    @property
    def spares(self):
        return {"tire_size": self._tire_size, "chain": self._chain}
