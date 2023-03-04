from __future__ import annotations

from src.money import Money


class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount, "USD")

    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)
