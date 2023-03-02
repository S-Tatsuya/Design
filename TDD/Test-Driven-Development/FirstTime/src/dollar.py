from __future__ import annotations
from typing import Any


class Dollar:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)

    def equals(self, object: Any):
        if hasattr(object, "_amount"):
            return self._amount == object._amount
        return False
