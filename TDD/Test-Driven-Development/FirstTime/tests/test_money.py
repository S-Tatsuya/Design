from src.dollar import Dollar
from src.franc import Franc


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        assert Dollar(10).equals(five.times(2))
        assert Dollar(15).equals(five.times(3))

    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))

    def test_franc_multiplication(self):
        five = Franc(5)
        assert Franc(10).equals(five.times(2))
        assert Franc(15).equals(five.times(3))
