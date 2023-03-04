from src.dollar import Dollar


class MoneyFactory:
    @staticmethod
    def dollar(amount):
        return Dollar(amount)
