class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self._chainring = chainring
        self._cog = cog
        self._rim = rim
        self._tire = tire

    @property
    def Ratio(self):
        return self._chainring / self._cog

    @property
    def GearInches(self):
        return self.Ratio * (self._rim + (self._tire * 2))


if __name__ == "__main__":
    # コンストラクタの引数を変更したためエラーとなる
    # print(Gear(52, 11).Ratio)
    # print(Gear(30, 27).Ratio)
    print(Gear(52, 11, 26, 1.5).GearInches)
    print(Gear(52, 11, 24, 1.25).GearInches)
