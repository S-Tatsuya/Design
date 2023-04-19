from src.Parts import Parts


class Bicycle:
    def __init__(self, **kwargs):
        self._size = kwargs.get("size")
        self._parts: Parts = kwargs.get("parts") or Parts([])

    @property
    def size(self):
        return self._size

    @property
    def default_chain(self):
        return "10-speed"

    @property
    def spares(self):
        return self._parts.spares

    @property
    def parts(self):
        return self._parts.parts
