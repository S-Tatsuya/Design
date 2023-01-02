class Bicycle:
    def __init__(self, **kwargs):
        self._style = kwargs["style"] if "style" in kwargs.keys() else "road"
        self._size = kwargs.get("size")
        self._tape_color = kwargs.get("tape_color")
        self._front_shock = kwargs.get("front_shock")
        self._rear_shock = kwargs.get("rear_shock")

    @property
    def size(self):
        return self._size

    @property
    def spares(self):
        if self._style == "road":
            return {
                "chain": "10-speed",
                "tire_size": "23",
                "tape_color": self._tape_color,
            }
        else:
            return {
                "chain": "10-speed",
                "tire_size": "2.1",
                "rear_shock": self._rear_shock,
            }
