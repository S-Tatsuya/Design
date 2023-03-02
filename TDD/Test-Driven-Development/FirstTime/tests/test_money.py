class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        Assert five.amount == 10
