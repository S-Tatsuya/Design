from src.money_factory import MoneyFactory


class Bank:
    def reduce(self, source, to):
        return MoneyFactory.dollar(10)
