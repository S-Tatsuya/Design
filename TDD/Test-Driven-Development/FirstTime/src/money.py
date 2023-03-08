from __future__ import annotations
from typing import Any
from src.expression import Expression
from src.sum import Sum


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self):
        return self._amount

    def equals(self, object: Any):
        if hasattr(object, "_amount"):
            return self._amount == object._amount and self._currency == object._currency
        return False

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Money) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self.currency(), to)
        return Money(self.amount / rate, to)
