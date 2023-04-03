class Mechanic:
    def prepare_trip(self, trip):
        for bicycle in trip.bicycles:
            self._prepare_bicycle(bicycle)

    def _prepare_bicycle(self, bicycle):
        bicycle.prepare()
