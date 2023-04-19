class Bicycle:
    def __init__(self):
        self._is_ready = False

    @property
    def is_ready(self):
        return self._is_ready

    def prepare(self):
        self._is_ready = True
