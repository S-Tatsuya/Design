class Driver:
    def gas_up(self, vehicle):
        vehicle.gas_ready()

    def fill_water_tank(self, vehicle):
        vehicle.fill_water_tank_ready()

    def is_ready(self, vehicle):
        return vehicle.is_ready()
