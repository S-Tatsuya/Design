class Gear:
    def __init__(self, chainring, cog):
        self.__chainring = chainring
        self.__cog = cog

    @property
    def Ratio(self):
        return self.__chainring / self.__cog

    def gearInches(self, diameter):
        return self.Ratio * diameter
