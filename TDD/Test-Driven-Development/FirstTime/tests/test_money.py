from src.dollar import Dollar


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        assert Dollar(10).equals(five.times(2))
        assert Dollar(15).equals(five.times(3))

    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
