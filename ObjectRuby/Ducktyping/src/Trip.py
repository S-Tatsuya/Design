from src.Bicycle import Bicycle
from src.Customer import Customer
from src.Vehicle import Vehicle
from src.Mechanic import Mechanic
from src.TripCoordinator import TripCoordinator
from src.Driver import Driver


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

    def prepare_ducktyping(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip(self)

    def prepare(self, prepares):
        for preparer in prepares:
            match preparer:
                case Mechanic():
                    preparer.prepare_bicycles(self._bicycles)

                case TripCoordinator():
                    preparer.buy_foods(self._customers)

                case Driver():
                    preparer.gas_up(self._vehicle)
                    preparer.fill_water_tank(self._vehicle)

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
