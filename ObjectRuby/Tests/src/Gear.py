from src.Wheel import Wheel


class Gear:
    def __init__(self, **kwargs):
        self._chainring = kwargs.get("chainring") or 0
        self._cog = kwargs.get("cog") or 0
        self._wheel = kwargs.get("wheel") or Wheel(0, 0)
        self._observer = kwargs.get("observer")

    def gear_inches(self):
        return self.ratio * self._wheel.diameter()

    @property
    def ratio(self):
        return self.chainring / self.cog

    @property
    def cog(self):
        return self._cog

    @cog.setter
    def cog(self, new_cog):
        self._cog = new_cog
        self.changed()

    @property
    def chainring(self):
        return self._chainring

    @chainring.setter
    def chainring(self, new_chainring):
        self._chainring = new_chainring
        self.changed()

    def changed(self):
        self._observer.changed(self.chainring, self.cog)
