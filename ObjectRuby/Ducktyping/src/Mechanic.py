class Mechanic:
    def prepare_bicycles(self, bicycles):
        for bicycle in bicycles:
            self.prepare_bicycle(bicycle)

    def prepare_bicycle(self, bicycle):
        bicycle.prepare()

    def is_ready(self, bicycles):
        for bicycle in bicycles:
            if not bicycle.is_ready():
                return False

        return True
