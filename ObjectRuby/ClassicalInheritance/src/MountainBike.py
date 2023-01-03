from src.Bicycle import Bicycle


class MountainBike(Bicycle):
    def __init__(self, **kwargs):
        self._front_shock = kwargs.get("front_shock")
        self._rear_shock = kwargs.get("rear_shock")
        super().__init__(**kwargs)

    @property
    def spares(self):
        result = super().spares
        result["rear_shock"] = self._rear_shock
        return result

    @property
    def default_tire_size(self):
        return "2.1"
