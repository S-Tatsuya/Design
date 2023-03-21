class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self._chainring = chainring
        self._cog = cog
        self._rim = rim
        self._tire = tire

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

    @property
    def rim(self):
        return self._rim

    @property
    def tire(self):
        return self._tire

    @property
    def ratio(self):
        return self.chainring / self.cog

    @property
    def gear_inches(self):
        return self.ratio * (self.rim + (self.tire * 2))


class ObscuringReferences:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    @property
    def diameters(self):
        return [(x[0] + (x[1] * 2)) for x in self.data]


if __name__ == "__main__":
    print(Gear(52, 11, 26, 1.5).ratio)
    print(Gear(30, 27, 24, 1.25).ratio)
    print(Gear(52, 11, 26, 1.5).gear_inches)
    print(Gear(30, 27, 24, 1.25).gear_inches)

    object = ObscuringReferences([[622, 20], [622, 23], [559, 30], [559, 40]])
    for diameters in object.diameters:
        print(diameters)
