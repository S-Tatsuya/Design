import src.chapter6_2 as sut


class TestChapter6_2:
    def test_bubble_sort1(self):
        test_data = [6, 4, 3, 7, 1, 9, 8]
        assert sut.bubble_sort1(test_data) == [1, 3, 4, 6, 7, 8, 9]

        test_data = [1, 3, 9, 4, 7, 8, 6]
        assert sut.bubble_sort1(test_data) == [1, 3, 4, 6, 7, 8, 9]
