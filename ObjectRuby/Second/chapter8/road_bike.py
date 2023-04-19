from bicycle import Bicycle


class RoadBike(Bicycle):
    def _post_initialize(self, **kwargs):
        self._style = kwargs.get("style", None)
        self._tape_color = kwargs.get("tape_color", None)

    @property
    def style(self):
        return self._style

    @property
    def tape_color(self):
        return self._tape_color

    def _local_spares(self):
        return {"tape_color": self.tape_color}

    def _default_tire_size(self):
        return "23"


if __name__ == "__main__":
    bike = RoadBike(style="road", size="M", tape_color="red")
    print(bike.spares())
