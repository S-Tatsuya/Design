from typing import Any


class Money:
    def __init__(self, amount):
        self._amount = amount

    def equals(self, object: Any):
        if hasattr(object, "_amount"):
            return self._amount == object._amount
        return False
