from __future__ import annotations
from typing import Any


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)

    def equals(self, object: Any):
        if hasattr(object, "amount"):
            return self.amount == object.amount
        return False
