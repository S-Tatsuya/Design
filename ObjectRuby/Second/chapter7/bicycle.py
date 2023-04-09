import datetime

from schedulable import Schedulable


class Bicycle(Schedulable):
    def _post_init(self):
        self._is_ready = False
        self._lead_days = 1

    @property
    def is_ready(self):
        return self._is_ready

    @property
    def lead_days(self):
        return datetime.timedelta(self._lead_days)

    def prepare(self):
        self._is_ready = True


if __name__ == "__main__":
    starting = datetime.date(2015, 9, 4)
    ending = datetime.date(2015, 9, 10)

    bicycle = Bicycle()
    bicycle.is_schedulable(starting, ending)
