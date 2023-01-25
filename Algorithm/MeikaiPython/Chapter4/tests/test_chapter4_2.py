import pytest

from src.chapter4_2 import FixedQueue


class TestChapter4_2:
    def test_fixed_queue(self):
        sut = FixedQueue()
        assert sut.is_empty()
        assert sut.is_full() is False
        assert sut.__len__() == 0

        sut.enque(1)

        assert sut.is_empty() is False
        assert sut.is_full() is False
        assert sut.__len__() == 1

        sut.enque(2)
        result = sut.deque()
        assert result == 1
        assert sut.is_empty() is False
        assert sut.__len__() == 1

        sut.enque(3)
        sut.enque(4)
        sut.enque(5)
        sut.enque(6)
        sut.enque(7)
        sut.enque(8)
        sut.enque(9)
        sut.enque(10)
        sut.enque(11)
        result = sut.deque()
        sut.enque(12)

        assert result == 2
        assert sut.is_full()
        assert sut.__len__()

    def test_full_expection(self):
        sut = FixedQueue(2)
        sut.enque(1)
        sut.enque(2)
        with pytest.raises(FixedQueue.Full) as e:
            sut.enque(3)

        assert str(e.value) == ""

    def test_empty_expection(self):
        sut = FixedQueue()
        with pytest.raises(FixedQueue.Empty) as e:
            sut.deque()

        assert str(e.value) == ""
