class Gear:
    # Wheelクラスを独立させる設計の根拠は明確ではないため、Gearクラスの一部として実装する
    class __Wheel:
        def __init__(self, rim, tire):
            self.__rim = rim
            self.__tire = tire

        @property
        def Diameter(self):
            return self.__rim + (self.__tire * 2)

    def __init__(self, chainring, cog, rim, tire):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = self.__Wheel(rim, tire)

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
    print(Gear(52, 11, 26, 1.5).GearInches)
    print(Gear(52, 11, 24, 1.25).GearInches)
