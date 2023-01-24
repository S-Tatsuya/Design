import pytest

from src.chapter4_1 import FixedStack


class TestChapter4_1:
    def test_fixed_stack(self):
        sut = FixedStack()
        assert sut.__len__() == 0
        assert len(sut) == 0

        sut.push(1)

        assert sut.__len__() == 1
        assert len(sut) == 1

        result = sut.pop()

        assert result == 1
        assert sut.__len__() == 0
        assert len(sut) == 0

    def test_full_exception(self):
        sut = FixedStack(2)

        assert sut.is_full() is False
        assert sut.is_empty()
        sut.push(1)
        sut.push(2)
        assert sut.is_full()
        assert sut.is_empty() is False

        with pytest.raises(FixedStack.Full) as e:
            sut.push(3)

        assert str(e.value) == ""

    def test_empty_exception(self):
        sut = FixedStack()
        assert sut.is_empty()
        with pytest.raises(FixedStack.Empty) as e:
            _ = sut.pop()

        assert str(e.value) == ""
