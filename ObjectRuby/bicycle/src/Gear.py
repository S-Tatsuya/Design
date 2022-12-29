from src.Wheel import Wheel


class Gear:
    def __init__(self, chainring, cog, wheel=Wheel(0, 0)):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel

    @property
    def Ratio(self):
        return self.__chainring / self.__cog

    @property
    def GearInches(self):
        return self.Ratio * self.__diameter()

    def __diameter(self):
        return self.__wheel.Diameter
