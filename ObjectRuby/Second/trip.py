from mechanic import Mechanic
from trip_coordinator import TripCoordinator
from driver import Driver


class Trip:
    def __init__(self, bicycles, customers, vehicle):
        self._bicycles = bicycles
        self._customers = customers
        self._vehicle = vehicle

    @property
    def bicycles(self):
        return self._bicycles

    @property
    def customers(self):
        return self._customers

    @property
    def vehicle(self):
        return self._vehicle

    def prepare(self, preparers):
        for preparer in preparers:
            if isinstance(preparer, Mechanic):
                preparer.prepare_bicycles(self.bicycles)
            elif isinstance(preparer, TripCoordinator):
                preparer.buy_food(self.customers)
            elif isinstance(preparer, Driver):
                preparer.gas_up(self.vehicle)

    def __str__(self):
        result = "Bicyles:"
        for bicycle in self.bicycles:
            result += str(bicycle.is_ready)
            result += ", "

        result += "\nCustomers:"
        for customer in self.customers:
            result += str(customer.is_ready)
            result += ", "

        result += "\nVehicle:"
        result += str(self.vehicle.is_ready)
        result += ", "

        return result
