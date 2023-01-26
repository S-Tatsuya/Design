import pytest

import src.chapter5_1 as sut


class TestChapter5_1:
    def test_factorial(self):
        assert sut.factorial(3) == 6
        assert sut.factorial(0) == 1

    def test_factorial_exception_value_error(self):
        with pytest.raises(ValueError) as e:
            sut.factorial(-1)

        assert str(e.value) == "負の数は受け付けません"
