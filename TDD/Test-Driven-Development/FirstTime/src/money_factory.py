from src.dollar import Dollar
from src.franc import Franc


class MoneyFactory:
    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)
