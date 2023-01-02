class Bicycle:
    def __init__(self, **kwargs):
        self._size = kwargs["size"]
        self._tape_color = kwargs["tape_color"]

    @property
    def size(self):
        return self._size

    @property
    def spares(self):
        return {"chain": "10-speed", "tire_size": "23", "tape_color": self._tape_color}
