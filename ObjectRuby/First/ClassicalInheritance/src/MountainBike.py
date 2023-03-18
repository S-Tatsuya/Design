from src.Bicycle import Bicycle


class MountainBike(Bicycle):
    @property
    def default_tire_size(self):
        return "2.1"

    def _post_initialize(self, **kwargs):
        self._front_shock = kwargs.get("front_shock")
        self._rear_shock = kwargs.get("rear_shock")

    def _local_spares(self):
        return {"rear_shock": self._rear_shock}
