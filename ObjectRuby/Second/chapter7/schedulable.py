import datetime
from abc import ABCMeta, abstractmethod

from schedule import Schedule


class Schedulable(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        self._schedule = kwargs.get("schedule", Schedule())
        self._post_init(**kwargs)

    @property
    def lead_days(self):
        return datetime.timedelta(0)

    @abstractmethod
    def _post_init(self):
        pass

    def is_schedulable(self, start_date, end_date):
        return self._schedule.is_scheduled(
            self, start_date - self.lead_days, end_date
        )  # type: ignore

    def is_shceduled(self, start_date, end_date):
        return self._schedule.is_scheduled(self, start_date, end_date)
