from abc import ABCMeta, abstractmethod


class Parts(metaclass=ABCMeta):
    def __init__(self, parts):
        self._parts = parts

    @property
    def _default_chain(self):
        return "10-speed"

    @property
    @abstractmethod
    def _default_tire_size(self):
        pass

    @property
    def spares(self):
        return {part.name: part.description for part in self._parts if part.needs_spare}

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
