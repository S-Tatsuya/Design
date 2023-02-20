import pytest

from src.chapter4_2 import FixedQueue, SampleQueue


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

        assert sut.peek() == 3

        assert sut.find(10) == 9
        assert sut.find(13) == -1

        assert sut.count(3) == 1
        sut.deque()
        assert sut.count(3) == 0
        sut.enque(7)
        assert sut.count(7) == 2

        assert 7 in sut
        assert 3 not in sut

        assert sut.is_full
        sut.clear()
        assert sut.is_empty()
        assert sut.is_full() is False
        assert sut.__len__() == 0

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

    def test_dump(self, capfd):
        sut = FixedQueue()
        sut.dump()
        out, err = capfd.readouterr()
        assert out == "キューは空です。\n"
        assert err == ""

        sut.enque(1)
        sut.enque(2)
        sut.enque(3)
        sut.enque(4)
        sut.enque(5)
        sut.deque()
        sut.dump()
        out, err = capfd.readouterr()
        assert out == "2 3 4 5 \n"
        assert err == ""

    def test_sample_queue(self, capfd):
        sut = SampleQueue()
        sut.enque(1)
        sut.enque(2)
        sut.enque(3)
        sut.enque(4)
        sut.enque(5)
        sut.enque(6)
        sut.enque(7)
        sut.enque(8)
        sut.enque(9)
        sut.enque(10)
        sut.dump()
        out, err = capfd.readouterr()
        assert out == "1 2 3 4 5 6 7 8 9 10 \n"
        assert err == ""

        sut.enque(11)
        sut.enque(12)
        sut.dump()
        out, err = capfd.readouterr()
        assert out == "3 4 5 6 7 8 9 10 12 13\n"
        assert err == ""
        sut.enque(13)
        sut.enque(14)
        sut.enque(15)
        sut.enque(16)
        sut.enque(17)
        sut.dump()
        out, err = capfd.readouterr()
        assert out == "8 9 10 12 13\n"
        assert err == ""
