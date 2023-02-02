import src.chapter6_7 as sut


class TestChapter6_7:
    def test_merge(self):
        test_data_a = [2, 4, 6, 8, 11, 13]
        test_data_b = [1, 2, 3, 4, 9, 16, 21]
        result_c = [None] * (len(test_data_a) + len(test_data_b))
        sut.merge(test_data_a, test_data_b, result_c)
        assert result_c == [1, 2, 2, 3, 4, 4, 6, 8, 9, 11, 13, 16, 21]

    def test_merge_sort(self):
        test_data = [5, 8, 4, 2, 6, 1, 3, 9, 7]
        assert sut.merge_sort(test_data) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
