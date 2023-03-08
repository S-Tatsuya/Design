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

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(MoneyFactory.dollar(1), "USD")
        assert MoneyFactory.dollar(1).equals(result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(MoneyFactory.franc(2), "USD")
        assert MoneyFactory.dollar(1).equals(result)

    def test_identity_rate(self):
        assert Bank().rate("USD", "USD") == 1

    def test_mixed_addition(self):
        fiveBucks: Expression = MoneyFactory.dollar(5)
        tenFrancs: Expression = MoneyFactory.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(fiveBucks.plus(tenFrancs), "USD")
        assert result.equals(MoneyFactory.dollar(10))
