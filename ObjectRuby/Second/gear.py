class Gear:
    def __init__(self, chainring, cog):
        self._chainring = chainring
        self._cog = cog

    @property
    def ratio(self):
        return self._chainring / self._cog


if __name__ == "__main__":
    print(Gear(52, 11).ratio)
    print(Gear(30, 27).ratio)
