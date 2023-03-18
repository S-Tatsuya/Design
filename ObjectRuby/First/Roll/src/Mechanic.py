from src.Schedulable import Schedulable


class Mechanic(Schedulable):
    def _set_lead_day(self):
        return 4
