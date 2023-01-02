from src.Trip import Trip


class TripCoordinator:
    def prepare_trip(self, trip: Trip):
        self.buy_foods(trip.Customers)

    def buy_foods(self, customers):
        for customer in customers:
            self.buy_food(customer)

    def buy_food(self, customer):
        customer.prepare()

    def is_ready(self, customers):
        for customer in customers:
            if not customer.is_ready():
                return False

        return True
