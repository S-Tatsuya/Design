from dataclasses import dataclass


class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self._chainring = chainring
        self._cog = cog
        self._wheel = Wheel(rim, tire)

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
    def rim(self):
        return self.wheel.rim

    @property
    def tire(self):
        return self.wheel.tire

    @property
    def ratio(self):
        return self.chainring / self.cog

    @property
    def gear_inches(self):
        return self.ratio * self.wheel.diameter


class RevealingReferences:
    def __init__(self, data):
        self._wheels = self._wheelify(data)

    @property
    def wheels(self):
        return self._wheels

    def _wheelify(self, data):
        return [Wheel(x[0], x[1]) for x in data]

    @property
    def diameters(self):
        return [wheel.diameter for wheel in self.wheels]


@dataclass
class Wheel:
    rim: int
    tire: int

    @property
    def diameter(self):
        return self.rim + (self.tire * 2)


if __name__ == "__main__":
    print(Gear(52, 11, 26, 1.5).ratio)
    print(Gear(30, 27, 24, 1.25).ratio)
    print(Gear(52, 11, 26, 1.5).gear_inches)
    print(Gear(30, 27, 24, 1.25).gear_inches)

    object = RevealingReferences([[622, 20], [622, 23], [559, 30], [559, 40]])
    for diameters in object.diameters:
        print(diameters)
