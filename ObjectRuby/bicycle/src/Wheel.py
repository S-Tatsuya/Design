import math


class Wheel:
    def __init__(self, rim, tire):
        self.__rim = rim
        self.__tire = tire

    @property
    def Diameter(self):
        return self.__rim + (self.__tire * 2)

    @property
    def Circumference(self):
        return self.Diameter * math.pi


if __name__ == "__main__":
    wheel = Wheel(26, 1.5)
    print(wheel.Circumference)


class Wheel2:
    def __init__(self, rim, tire):
        self.__rim = rim
        self.__tire = tire

    @property
    def Diameter(self):
        return self.__rim + (self.__tire * 2)
