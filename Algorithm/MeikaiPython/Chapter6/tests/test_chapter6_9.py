import src.chapter6_9 as sut


class TestChapter6_9:
    def test_counting_sort(self):
        test_data = [22, 5, 11, 32, 99, 68, 70]
        assert sut.counting_sort(test_data, 100) == [
            5,
            11,
            22,
            32,
            68,
            70,
            99,
        ]
