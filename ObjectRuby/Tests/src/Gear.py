from src.Wheel import Wheel


class Gear:
    def __init__(self, **kwargs):
        self._chainring = kwargs.get("chainring") or 0
        self._cog = kwargs.get("cog") or 0
        self._wheel = kwargs.get("wheel") or Wheel(0, 0)

    def gear_inches(self):
        return self.ratio * self._wheel.diameter()

    @property
    def ratio(self):
        return self._chainring / self._cog
