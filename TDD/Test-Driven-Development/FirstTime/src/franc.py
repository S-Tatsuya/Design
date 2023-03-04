from __future__ import annotations

from src.money import Money


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount, "CHF")

    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)

    def currency(self) -> str:
        return self._currency
