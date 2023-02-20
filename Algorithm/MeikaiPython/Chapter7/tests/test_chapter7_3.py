import src.chapter7_3 as sut


class TestChapter7_3:
    def test_bm_match(self):
        test_data_match = "ABABCDEFGHA"
        test_data_unmatch = "ABABADEFGHA"
        assert sut.bm_match(test_data_match, "ABC") == 2
        assert sut.bm_match(test_data_unmatch, "ABC") == -1
