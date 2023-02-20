import src.chapter6_8 as sut


class TestChapter6_8:
    def test_heap_sort(self):
        test_data = [6, 4, 3, 7, 1, 9, 8]
        assert sut.heap_sort(test_data) == [1, 3, 4, 6, 7, 8, 9]
