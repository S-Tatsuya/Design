import src.chapter6_3 as sut


class TestChapter6_3:
    def test_selection_sort(self):
        test_data = [6, 4, 8, 3, 1, 9, 7]
        assert sut.selection_sort(test_data) == [1, 3, 4, 6, 7, 8, 9]
