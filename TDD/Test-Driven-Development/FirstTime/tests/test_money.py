from src.money_factory import MoneyFactory
from src.expression import Expression
from src.bank import Bank
from src.sum import Sum


class TestMoney:
    def test_multiplication(self):
        five = MoneyFactory.dollar(5)
        assert MoneyFactory.dollar(10).equals(five.times(2))
        assert MoneyFactory.dollar(15).equals(five.times(3))

    def test_equality(self):
        assert MoneyFactory.dollar(5).equals(MoneyFactory.dollar(5))
        assert not MoneyFactory.dollar(5).equals(MoneyFactory.dollar(6))
        assert not MoneyFactory.franc(5).equals(MoneyFactory.dollar(5))

    def test_currency(self):
        assert MoneyFactory.dollar(1).currency() == "USD"
        assert MoneyFactory.franc(1).currency() == "CHF"

    def test_simple_addition(self):
        five = MoneyFactory.dollar(5)
        sum: Expression = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        assert MoneyFactory.dollar(10).equals(reduced)

    def test_plus_returns_sum(self):
        five = MoneyFactory.dollar(5)
        result = five.plus(five)
        sum = result
        assert five.equals(sum.augend)
        assert five.equals(sum.addend)

    def test_reduce_sum(self):
        sum = Sum(MoneyFactory.dollar(3), MoneyFactory.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        assert MoneyFactory.dollar(7).equals(result)
