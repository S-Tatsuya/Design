from bicycle import Bicycle


class MountainBike(Bicycle):
    def _post_initialize(self, **kwargs):
        self._front_shock = kwargs.get("front_shock", None)
        self._rear_shock = kwargs.get("rear_shock", None)

    @property
    def front_shock(self):
        return self._front_shock

    @property
    def rear_shock(self):
        return self._rear_shock

    def _local_spares(self):
        return {"rear_shock": self.rear_shock}

    def _default_tire_size(self):
        return "2.1"


if __name__ == "__main__":
    bike = MountainBike(
        style="mountain", size="S", front_shock="Manitou", rear_shock="Fox"
    )
    print(bike.size)
    print(bike.spares())
