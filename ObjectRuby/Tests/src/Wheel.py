class Wheel:
    def __init__(self, rim, tire):
        self._rim = rim
        self._tire = tire

    def diameter(self):
        return self._rim + (self._tire * 2)
