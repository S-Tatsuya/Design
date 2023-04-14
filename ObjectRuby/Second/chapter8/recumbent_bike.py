from bicycle import Bicycle


class RecumbentBike(Bicycle):
    def _post_initialize(self, **kwargs):
        self._flag = kwargs.get("flag", None)

    @property
    def flag(self):
        return self._flag

    def _local_spares(self):
        return {"flag": self.flag}

    def _default_tire_size(self):
        return "28"

    def _default_chain(self):
        return "9-speed"


if __name__ == "__main__":
    bike = RecumbentBike(flag="tall and orange")
    print(bike.spares())
