class TripCoordinator:
    def prepare_trip(self, trip):
        for customer in trip.customers:
            self._prepare_food(customer)

    def _prepare_food(self, customer):
        customer.prepare()
