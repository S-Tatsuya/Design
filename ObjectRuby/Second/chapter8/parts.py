class Parts:
    def __init__(self, parts):
        self._parts = parts

    @property
    def parts(self):
        return self._parts

    def spares(self):
        return [part for part in self.parts if part.needs_spare]

    def __len__(self):
        return len(self.parts)

    def __iter__(self):
        return iter(self.parts)


class RoadBikeParts(Parts):
    def post_initialize(self, **kwargs):
        self._tape_color = kwargs.get("tape_color", self._default_tape_color())

    @property
    def tape_color(self):
        return self._tape_color

    def local_spares(self):
        return {"tape_color": self.tape_color}

    def _default_tire_size(self):
        return "23"

    def _default_chain(self):
        return "10-speed"

    def _default_tape_color(self):
        return "red"


class MountainBikeParts(Parts):
    def post_initialize(self, **kwargs):
        self._front_shock = kwargs.get("front_shock", self._default_front_shock())
        self._rear_shock = kwargs.get("rear_shock", self._default_rear_shock())

    @property
    def rear_shock(self):
        return self._rear_shock

    def local_spares(self):
        return {"rear_shock": self.rear_shock}

    def _default_front_shock(self):
        return "Manitou"

    def _default_rear_shock(self):
        return "Fox"

    def _default_tire_size(self):
        return "2.1"

    def _default_chain(self):
        return "10-speed"
