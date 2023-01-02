class Vehicle:
    def __init__(self):
        self._is_gas_ready = False
        self._is_water_tank_ready = False

    def gas_ready(self):
        self._is_gas_ready = True

    def fill_water_tank_ready(self):
        self._is_water_tank_ready = True

    def is_ready(self):
        return self._is_gas_ready and self._is_water_tank_ready
