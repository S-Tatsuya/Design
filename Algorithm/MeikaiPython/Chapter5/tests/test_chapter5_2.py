import src.chapter5_2 as sut


class TestChapter5_2:
    def test_recur1(self, capfd):
        sut.recur1(4)
        out, err = capfd.readouterr()
        assert out == "1\n2\n3\n1\n4\n1\n2\n"
        assert err == ""

    def test_recur(self, capfd):
        sut.recur(4)
        out, err = capfd.readouterr()
        assert out == "1\n2\n3\n1\n4\n1\n2\n"
        assert err == ""

    def test_recur1b(self, capfd):
        sut.recur1b(4)
        out, err = capfd.readouterr()
        assert out == "1\n2\n3\n1\n4\n1\n2\n"
        assert err == ""
