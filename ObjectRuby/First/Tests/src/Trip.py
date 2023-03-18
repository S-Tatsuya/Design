from src.PrepareTarget import Bicycle, Customer, Vehicle


class Trip:
    def __init__(self):
        self._bicycles = [Bicycle(), Bicycle(), Bicycle()]
        self._customers = [Customer(), Customer(), Customer(), Customer()]
        self._vehicles = [Vehicle(), Vehicle(), Vehicle()]

    def prepare(self, preparers):
        for prepare in preparers:
            prepare.prepare_trip(self)

    @property
    def bicycles(self):
        return self._bicycles

    @property
    def customers(self):
        return self._customers

    @property
    def vehicles(self):
        return self._vehicles
