from src.chapter4_2 import FixedQueue


class TestChapter4_2:
    def test_fixed_queue(self):
        sut = FixedQueue(10)
        assert sut.is_empty()
        assert sut.is_full() is False
        assert sut.__len__() == 0
