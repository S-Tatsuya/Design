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

        sut.push(2)
        sut.push(3)
        result = sut.peek()
        assert result == 3
        assert len(sut) == 2

        sut.clear()
        assert sut.is_empty()
        assert sut.__len__() == 0

        sut.push(4)
        sut.push(5)
        sut.push(6)

        assert sut.find(5) == 1
        assert sut.find(7) == -1

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

        with pytest.raises(FixedStack.Empty) as e:
            _ = sut.peek()

        assert str(e.value) == ""
