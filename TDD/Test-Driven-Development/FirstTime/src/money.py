from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any


class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def equals(self, object: Any):
        if hasattr(object, "_amount"):
            return self._amount == object._amount and type(self) == type(object)
        return False

    @abstractmethod
    def times(self, multipliner: int) -> Money:
        pass

    @abstractmethod
    def currency(self) -> str:
        pass
