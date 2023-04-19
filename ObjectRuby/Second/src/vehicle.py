class Vehicle:
    def __init__(self):
        self._is_gas_ready = False

    @property
    def is_ready(self):
        return self._is_gas_ready

    def gas_up(self):
        self._is_gas_ready = True
