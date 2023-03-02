from src.dollar import Dollar


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        assert product.amount == 10
        product = five.times(3)
        assert product.amount == 15

    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
