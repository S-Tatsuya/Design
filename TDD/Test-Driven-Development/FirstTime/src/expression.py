from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def plus(self, added: Expression):
        pass

    @abstractmethod
    def reduce(self, bank, to):
        pass

    @abstractmethod
    def times(self, multiplier):
        pass
