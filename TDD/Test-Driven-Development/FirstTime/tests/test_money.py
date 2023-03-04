from src.money_factory import MoneyFactory


class TestMoney:
    def test_multiplication(self):
        five = MoneyFactory.dollar(5)
        assert MoneyFactory.dollar(10).equals(five.times(2))
        assert MoneyFactory.dollar(15).equals(five.times(3))

    def test_equality(self):
        assert MoneyFactory.dollar(5).equals(MoneyFactory.dollar(5))
        assert not MoneyFactory.dollar(5).equals(MoneyFactory.dollar(6))
        assert MoneyFactory.franc(5).equals(MoneyFactory.franc(5))
        assert not MoneyFactory.franc(5).equals(MoneyFactory.franc(6))
        assert not MoneyFactory.franc(5).equals(MoneyFactory.dollar(5))

    def test_franc_multiplication(self):
        five = MoneyFactory.franc(5)
        assert MoneyFactory.franc(10).equals(five.times(2))
        assert MoneyFactory.franc(15).equals(five.times(3))

    def test_currency(self):
        assert MoneyFactory.dollar(1).currency() == "USD"
        assert MoneyFactory.franc(1).currency() == "CHF"
