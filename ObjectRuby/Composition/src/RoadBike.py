from src.Bicycle import Bicycle


class RoadBike(Bicycle):
    @property
    def spares(self):
        result = super().spares
        return result

    @property
    def default_tire_size(self):
        return "23"

    def _post_initialize(self, **kwargs):
        self._tape_color = kwargs.get("tape_color")

    def _local_spares(self):
        return {"tape_color": self._tape_color}
