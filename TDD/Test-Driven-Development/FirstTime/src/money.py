from __future__ import annotations
from typing import Any

from src.expression import Expression


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def equals(self, object: Any):
        if hasattr(object, "_amount"):
            return self._amount == object._amount and self._currency == object._currency
        return False

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Money) -> Expression:
        return Money(self._amount + addend._amount, self._currency)
