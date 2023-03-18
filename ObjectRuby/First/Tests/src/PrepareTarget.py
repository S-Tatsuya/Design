class PrepareTarget:
    def __init__(self):
        self._is_prepare = False
        self._name = self._set_name()

    def is_prepare(self):
        print(self._name)
        return self._is_prepare

    def prepare(self):
        self._is_prepare = True

    def _set_name(self):
        return "default"


class Bicycle(PrepareTarget):
    def _set_name(self):
        return "Bicycle"


class Customer(PrepareTarget):
    def _set_name(self):
        return "Customer"


class Vehicle(PrepareTarget):
    def _set_name(self):
        return "Vehicle"
