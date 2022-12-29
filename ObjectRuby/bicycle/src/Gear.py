from Wheel import Wheel


class Gear:
    def __init__(self, chainring, cog, wheel: Wheel = Wheel(0, 0)):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel

    @property
    def Ratio(self):
        return self.__chainring / self.__cog

    @property
    def GearInches(self):
        return self.Ratio * self.__wheel.Diameter


if __name__ == "__main__":
    # コンストラクタの引数を変更したためエラーとなる
    # print(Gear(52, 11).Ratio)
    # print(Gear(30, 27).Ratio)

    wheel = Wheel(26, 1.5)
    print(wheel.Circumference)

    gear = Gear(52, 11, wheel)
    print(gear.Ratio)
    print(gear.GearInches)
    gear = Gear(52, 11)
    print(gear.Ratio)
    print(gear.GearInches)
