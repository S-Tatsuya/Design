import src.chapter7_1 as sut


class TestChapter7:
    def test_bf_match(self):
        test_data_match = "ABABCDEFGHA"
        test_data_unmatch = "ABABADEFGHA"
        assert sut.bf_match(test_data_match, "ABC") == 2
        assert sut.bf_match(test_data_unmatch, "ABC") == -1
