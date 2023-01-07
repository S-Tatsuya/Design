from src.Schedulable import Schedulable


class Vehicle(Schedulable):
    def _set_lead_day(self):
        return 3
