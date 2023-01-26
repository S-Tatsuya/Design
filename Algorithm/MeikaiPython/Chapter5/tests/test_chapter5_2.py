import src.chapter5_2 as sut


class TestChapter5_2:
    def test_crecur1(self, capfd):
        sut.recur1(4)
        out, err = capfd.readouterr()
        assert out == "1\n2\n3\n1\n4\n1\n2\n"
        assert err == ""
