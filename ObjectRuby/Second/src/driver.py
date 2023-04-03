class Driver:
    def prepare_trip(self, trip):
        self._gas_up(trip.vehicle)

    def _gas_up(self, vehicle):
        vehicle.gas_up()
