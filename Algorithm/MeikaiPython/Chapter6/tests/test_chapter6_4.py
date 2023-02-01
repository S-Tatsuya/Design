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

    def test_partition(self, capfd):
        test_data = [1, 8, 7, 4, 5, 2, 6, 3, 9]
        sut.partition(test_data)
        out, err = capfd.readouterr()
        assert out == (
            "枢軸の値は5です。\n"
            "枢軸以下のグループ\n"
            "1 3 2 4 5\n"
            "枢軸と一致するグループ\n"
            "5\n"
            "枢軸以上のグループ\n"
            "5 7 6 8 9\n"
        )
        assert err == ""

    def test_quick_sort(self):
        test_data = [5, 8, 4, 2, 6, 1, 3, 9, 7]
        sut.quick_sort(test_data, 0, len(test_data) - 1)
        assert test_data == [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
        ]
