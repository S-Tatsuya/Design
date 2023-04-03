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
            preparer.prepare_trip(self)

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
