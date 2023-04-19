class Customer:
    def __init__(self):
        self._is_ready = False

    def prepare(self):
        self._is_ready = True

    def is_ready(self):
        return self._is_ready
