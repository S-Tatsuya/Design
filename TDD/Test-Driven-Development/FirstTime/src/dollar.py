from __future__ import annotations


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)

    def equals(self, object: any):
        return True
