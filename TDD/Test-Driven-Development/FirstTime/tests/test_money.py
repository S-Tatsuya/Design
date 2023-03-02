from src.dollar import Dollar


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        assert five.amount == 10
