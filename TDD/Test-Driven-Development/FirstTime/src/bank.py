from src.money_factory import MoneyFactory


class Bank:
    def reduce(self, source, to):
        sum = source
        amount = sum.augend.amount + sum.addend.amount
        return MoneyFactory.money(amount, to)
