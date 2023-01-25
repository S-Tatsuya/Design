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

    def test_full_expection(self):
        sut = FixedQueue(2)
        sut.enque(1)
        sut.enque(2)
        with pytest.raises(FixedQueue.Full) as e:
            sut.enque(3)

        assert str(e.value) == ""
