from src.money_factory import MoneyFactory
from src.franc import Franc


class TestMoney:
    def test_multiplication(self):
        five = MoneyFactory.dollar(5)
        assert MoneyFactory.dollar(10).equals(five.times(2))
        assert MoneyFactory.dollar(15).equals(five.times(3))

    def test_equality(self):
        assert MoneyFactory.dollar(5).equals(MoneyFactory.dollar(5))
        assert not MoneyFactory.dollar(5).equals(MoneyFactory.dollar(6))
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))
        assert not Franc(5).equals(MoneyFactory.dollar(5))

    def test_franc_multiplication(self):
        five = Franc(5)
        assert Franc(10).equals(five.times(2))
        assert Franc(15).equals(five.times(3))
