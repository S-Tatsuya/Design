import datetime
from abc import ABCMeta
from src.Schedule import Schedule


class Schedulable(metaclass=ABCMeta):
    def __init__(self):
        self._lead_day = self._set_lead_day()

    def is_schedulable(self, starting, ending):
        return self._is_scheduled(starting - self.lead_day, ending)

    @property
    def schedule(self):
        return Schedule()

    @property
    def lead_day(self):
        return datetime.timedelta(days=self._lead_day)

    def _set_lead_day(self):
        return 0

    def _is_scheduled(self, start_date, end_date):
        return self.schedule.is_schedulable(self, start_date, end_date)
