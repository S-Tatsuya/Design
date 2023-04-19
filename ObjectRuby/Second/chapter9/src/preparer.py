class Mechanic:
    def prepare_trip(self, trip):
        for bicycle in trip.bicycles:
            self.prepare_bicycle(bicycle)

    def prepare_bicycle(self, bicycle):  # pyright: ignore
        pass


class TripCoordinator:
    def prepare_trip(self, trip):
        self.buy_food(trip.customers)

    def buy_food(self, customers):  # pyright: ignore
        pass


class Driver:
    def prepare_trip(self, trip):
        self.gas_up(trip.vehicle)

    def gas_up(self, vehicle):  # pyright: ignore
        pass


class Trip:
    def __init__(self, **kwargs):
        self.bicycles = kwargs.get("bicycles")
        self.customers = kwargs.get("customers")
        self.vehicle = kwargs.get("vehicle")

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip(self)
