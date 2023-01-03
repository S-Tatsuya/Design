from src.Bicycle import Bicycle


class RoadBike(Bicycle):
    def __init__(self, **kwargs):
        self._tape_color = kwargs.get("tape_color")
        super().__init__(**kwargs)

    @property
    def spares(self):
        return {"chain": "10-speed", "tire_size": "23", "tape_color": self._tape_color}

    @property
    def default_tire_size(self):
        return "23"
