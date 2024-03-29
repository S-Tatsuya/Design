from src.expression import Expression
import src.money_factory as MoneyFactory


class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression):
        self.augend: Expression = augend
        self.addend: Expression = addend

    def reduce(self, bank, to):
        amount = (
            self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        )
        return MoneyFactory.MoneyFactory.money(amount, to)

    def plus(self, added: Expression):
        return Sum(self, added)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))
