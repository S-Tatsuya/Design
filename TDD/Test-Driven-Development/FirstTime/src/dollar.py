from __future__ import annotations
from typing import Any

from src.money import Money


class Dollar(Money):
    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)

    def equals(self, object: Any):
        if hasattr(object, "_amount"):
            return self._amount == object._amount
        return False
