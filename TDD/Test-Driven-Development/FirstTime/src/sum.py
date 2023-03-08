from src.expression import Expression
import src.money_factory as MoneyFactory


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend.amount + self.addend.amount
        return MoneyFactory.MoneyFactory.money(amount, to)
