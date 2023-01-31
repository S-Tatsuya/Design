import src.chapter6_4 as sut


class TestChapter6_4:
    def test_insertion_sort(self):
        test_data = [6, 4, 3, 7, 1, 9, 8]
        assert sut.insertion_sort(test_data) == [1, 3, 4, 6, 7, 8, 9]

    def test_binary_insertion_sort(self):
        test_data = [6, 4, 3, 7, 1, 9, 8]
        assert sut.binary_insertion_sort(test_data) == [1, 3, 4, 6, 7, 8, 9]

    def test_shell_sort(self):
        test_data = [6, 4, 3, 7, 1, 9, 8]
        assert sut.shell_sort(test_data) == [1, 3, 4, 6, 7, 8, 9]
