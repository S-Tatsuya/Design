from __future__ import annotations
from typing import Any


class Franc:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)

    def equals(self, object: Any):
        if hasattr(object, "_amount"):
            return self._amount == object._amount
        return False
