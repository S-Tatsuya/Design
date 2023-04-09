import datetime

from schedulable import Schedulable


class Vehicle(Schedulable):
    def _post_init(self):
        self._is_gas_ready = False
        self._lead_days = 3

    @property
    def is_ready(self):
        return self._is_gas_ready

    @property
    def lead_days(self):
        return datetime.timedelta(self._lead_days)

    def gas_up(self):
        self._is_gas_ready = True


if __name__ == "__main__":
    starting = datetime.date(2015, 9, 4)
    ending = datetime.date(2015, 9, 10)

    v = Vehicle()
    v.is_schedulable(starting, ending)
