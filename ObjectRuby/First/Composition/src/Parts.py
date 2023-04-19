class Parts:
    def __init__(self, parts):
        self._parts = parts

    @property
    def spares(self):
        return {part.name: part.description for part in self._parts if part.needs_spare}

    @property
    def parts(self):
        return [(part.name, part.description, part.needs_spare) for part in self._parts]
