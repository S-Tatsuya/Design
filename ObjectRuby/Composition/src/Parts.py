from abc import ABCMeta, abstractmethod


class Parts(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        self._chain = kwargs.get("chain") or self._default_chain
        self._tire_size = kwargs.get("tire_size") or self._default_tire_size

        self._post_initialize(**kwargs)

    @property
    def chain(self):
        return self._chain

    @property
    def tire_size(self):
        return self._tire_size

    @property
    def _default_chain(self):
        return "10-speed"

    @property
    @abstractmethod
    def _default_tire_size(self):
        pass

    @property
    def spares(self):
        result = {"tire_size": self._tire_size, "chain": self._chain}
        result.update(self._local_spares())
        return result

    @abstractmethod
    def _post_initialize(self, **kwargs):
        pass

    @abstractmethod
    def _local_spares(self) -> dict:
        pass


class RoadBikeParts(Parts):
    @property
    def _default_tire_size(self):
        return "23"

    def _post_initialize(self, **kwargs):
        self._tape_color = kwargs.get("tape_color")

    def _local_spares(self):
        return {"tape_color": self._tape_color}


class MountainBikeParts(Parts):
    @property
    def _default_tire_size(self):
        return "2.1"

    @property
    def rear_shock(self):
        return self._rear_shock

    def _post_initialize(self, **kwargs):
        self._front_shock = kwargs.get("front_shock")
        self._rear_shock = kwargs.get("rear_shock")

    def _local_spares(self):
        return {"rear_shock": self.rear_shock}


class RecumbentBikeParts(Parts):
    @property
    def _default_chain(self):
        return "9-speed"

    @property
    def _default_tire_size(self):
        return "28"

    @property
    def flag(self):
        return self._flag

    def _post_initialize(self, **kwargs):
        self._flag = kwargs.get("flag")

    def _local_spares(self):
        return {"flag": self.flag}
