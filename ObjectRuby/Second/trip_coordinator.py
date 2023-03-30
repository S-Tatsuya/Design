class TripCoordinator:
    def buy_food(self, customers):
        customers = list(map(self._prepare_food, customers))

    def _prepare_food(self, customer):
        customer.prepare()
