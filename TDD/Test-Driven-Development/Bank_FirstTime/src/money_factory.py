from src.money import Money


class MoneyFactory:
    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    @staticmethod
    def money(amount, currency):
        return Money(amount, currency)
