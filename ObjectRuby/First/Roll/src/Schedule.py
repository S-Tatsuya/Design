class Schedule:
    def is_schedulable(self, target, starting, ending):
        print(
            f"This {target.__class__.__name__} is not scheduled\n"
            + f"between {starting} and {ending}."
        )
        return False
