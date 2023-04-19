class Wheel:
    def __init__(self, rim, tire):
        self._rim = rim
        self._tire = tire

    @property
    def rim(self):
        return self._rim

    @property
    def tire(self):
        return self._tire

    def width(self):
        return self.rim + (self.tire * 2)


class Gear:
    def __init__(self, **kwargs):
        self._chainring = kwargs.get("chainring", 0)
        self._cog = kwargs.get("cog", 0)
        self._wheel = kwargs.get("wheel", 0)
        self._observer = kwargs.get("observer", None)

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

    @property
    def wheel(self):
        return self._wheel

    @property
    def gear_inches(self):
        return self.ratio * self.wheel.diameter()  # pyright: ignore

    @property
    def observer(self):
        return self._observer

    @property
    def ratio(self):
        return self.chainring / self.cog

    @cog.setter
    def cog(self, new_cog):
        self._cog = new_cog
        self.changed()

    @chainring.setter
    def chainring(self, new_chainring):
        self._chainring = new_chainring
        self.changed()

    def changed(self):
        self.observer.changed(self.chainring, self.cog)  # type: ignore
