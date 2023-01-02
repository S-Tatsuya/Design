from src.Bicycle import Bicycle
from src.Customer import Customer
from src.Vehicle import Vehicle


class Trip:
    def __init__(self):
        self._bicycles = [Bicycle(), Bicycle(), Bicycle()]
        self._customers = [Customer(), Customer(), Customer()]
        self._vehicle = Vehicle()

    @property
    def Bicycles(self):
        return self._bicycles

    @property
    def Customers(self):
        return self._customers

    @property
    def Vehicle(self):
        return self._vehicle

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip(self)

    def is_ready(self):
        return (
            self.is_ready_bicycles()
            and self.is_ready_customers()
            and self.is_ready_vehicle()
        )

    def is_ready_bicycles(self):
        for bicycle in self._bicycles:
            if not bicycle.is_ready():
                return False

        return True

    def is_ready_customers(self):
        for customer in self._customers:
            if not customer.is_ready():
                return False

        return True

    def is_ready_vehicle(self):
        return self._vehicle.is_ready()
