from src.PrepareTarget import Bicycle, Customer, Vehicle
from src.Trip import Trip


class Mechanic:
    def prepare_trips(self, trip: Trip):
        for bicycle in trip.bicycles:
            self.prepare(bicycle)

    def prepare(self, bicycle: Bicycle):
        bicycle.prepare()


class TripCoordinator:
    def prepare_trips(self, trip: Trip):
        for customer in trip.customers:
            self.buy_food(customer)

    def buy_food(self, customer: Customer):
        customer.prepare()


class Driver:
    def prepare_trips(self, trip: Trip):
        for vehicle in trip.vehicles:
            self.prepare(vehicle)

    def prepare(self, vehicle: Vehicle):
        vehicle.prepare()
