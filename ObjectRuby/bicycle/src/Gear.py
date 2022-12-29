from src.Wheel import Wheel


class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self.__chainring = chainring
        self.__cog = cog
        self.__rim = rim
        self.__tire = tire

    @property
    def Ratio(self):
        return self.__chainring / self.__cog

    @property
    def GearInches(self):
        return self.Ratio * Wheel(self.__rim, self.__tire).Diameter
