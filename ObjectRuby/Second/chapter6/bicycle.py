from abc import ABCMeta, abstractmethod


class Bicycle(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        self._size = kwargs.get("size", None)
        self._chain = kwargs.get("chain", self._default_chain())
        self._tire_size = kwargs.get("tire_size", self._default_tire_size())

        self._post_initialize(**kwargs)

    @property
    def size(self):
        return self._size

    @property
    def chain(self):
        return self._chain

    @property
    def tire_size(self):
        return self._tire_size

    def spares(self):
        return {
            **{"tire_size": self.tire_size, "chain": self.chain},
            **self._local_spares(),
        }

    def _default_chain(self):
        return "10-speed"

    @abstractmethod
    def _default_tire_size(self):
        pass

    @abstractmethod
    def _post_initialize(self, **kwargs):
        pass

    @abstractmethod
    def _local_spares(self) -> dict:
        pass
