import src.chapter7_2 as sut


class TestChapter7_2:
    def test_kmp_match(self):
        test_data_match = "ZABCABDACCADEF"
        test_data_unmatch = "ZABCABXACCADEF"
        assert sut.kmp_match(test_data_match, "ABCABD") == 1
        assert sut.kmp_match(test_data_unmatch, "ABCABD") == -1
