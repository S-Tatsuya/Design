from src.Bicycle import Bicycle


class RecumbentBike(Bicycle):
    @property
    def default_tire_size(self):
        return "28"

    @property
    def default_chain(self):
        return "9-speed"

    def _post_initialize(self, **kwargs):
        self._flag = kwargs.get("flag")

    def _local_spares(self):
        return {"flag": self._flag}
