import src.chapter5_1 as sut


class TestChapter5_1:
    def test_factorial(self):
        assert sut.factorial(3) == 6
