import datetime

from schedulable import Schedulable


class Mechanic(Schedulable):
    def _post_init(self):
        self._lead_days = 4

    def prepare_trip(self, trip):
        for bicycle in trip.bicycles:
            self._prepare_bicycle(bicycle)

    def _prepare_bicycle(self, bicycle):
        bicycle.prepare()

    @property
    def lead_days(self):
        return datetime.timedelta(self._lead_days)


if __name__ == "__main__":
    starting = datetime.date(2015, 9, 4)
    ending = datetime.date(2015, 9, 10)

    m = Mechanic()
    m.is_schedulable(starting, ending)
