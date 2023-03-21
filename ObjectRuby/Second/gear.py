class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self._chainring = chainring
        self._cog = cog
        self._rim = rim
        self._tire = tire

    @property
    def ratio(self):
        return self._chainring / self._cog

    @property
    def gear_inches(self):
        return self.ratio * (self._rim + (self._tire * 2))


if __name__ == "__main__":
    print(Gear(52, 11, 26, 1.5).ratio)
    print(Gear(30, 27, 24, 1.25).ratio)
    print(Gear(52, 11, 26, 1.5).gear_inches)
    print(Gear(30, 27, 24, 1.25).gear_inches)
