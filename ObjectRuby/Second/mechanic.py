class Mechanic:
    def prepare_bicycles(self, bicycles):
        bicycles = list(map(self._prepare_bicycle, bicycles))

    def _prepare_bicycle(self, bicycle):
        bicycle.prepare()
