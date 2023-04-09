class Schedule:
    def is_scheduled(self, shedulable, starting, ending):
        print(
            f"This {type(shedulable).__name__} is not "
            f"scheduled between {starting} and {ending}"
        )

    def add(self, target, starting, ending):
        pass

    def remove(self, target, starting, ending):
        pass
