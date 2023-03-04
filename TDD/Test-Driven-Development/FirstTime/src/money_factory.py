from src.dollar import Dollar
from src.franc import Franc


class MoneyFactory:
    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")
