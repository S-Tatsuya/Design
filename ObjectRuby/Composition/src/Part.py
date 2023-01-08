class Part:
    def __init__(self, **kwargs):
        self._name = kwargs.get("name")
        self._description = kwargs.get("description")
        self._needs_spare = (
            kwargs.get("needs_spare") if kwargs.get("needs_spare") is False else True
        )

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def needs_spare(self):
        return self._needs_spare
