import io

import src.chapter1_2 as sut


class TestChapter1_2:
    def test_sum1ton_while(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
        sut.sum1ton_while()
        out, err = capfd.readouterr()

        assert out == "1からnまでの総和を求めます。\nnの値:1から5までの総和は15です。\n"
        assert err == ""

    def test_sum1ton_while(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
        sut.sum1ton_for()
        out, err = capfd.readouterr()

        assert out == "1からnまでの総和を求めます。\nnの値:1から5までの総和は15です。\n"
        assert err == ""

    def test_sum_gauss(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
        sut.sum_gauss()
        out, err = capfd.readouterr()

        assert out == "1からnまでの総和を求めます。\nnの値:1から5までの総和は15です。\n"
        assert err == ""
