from src.Bicycle import Bicycle


class Trip:
    def __init__(self):
        self._bicycles = [Bicycle(), Bicycle(), Bicycle()]
        self._customers = []
        self._vehicle = ""

    def prepar(self, mechanic):
        mechanic.prepare_bicycles(self._bicycles)

    def is_ready(self):
        for bicycle in self._bicycles:
            print(bicycle.is_ready())
            if not bicycle.is_ready():
                return False

        return True
