import io

import src.chapter1_2 as sut


class TestChapter1_2:
    def test_sum1ton_while(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
        sut.sum1ton_while()
        out, err = capfd.readouterr()

        assert out == "1からnまでの総和を求めます。\nnの値:1から5までの総和は15です。\n"
        assert err == ""

    def test_sum1ton_for(self, monkeypatch, capfd):
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

    def test_sum(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("3\n8\n"))
        sut.sum()
        out, err = capfd.readouterr()

        assert out == "aからbまでの総和を求めます。\n整数a:整数b:3から8までの総和は33です。\n"
        assert err == ""

        monkeypatch.setattr("sys.stdin", io.StringIO("8\n3\n"))
        sut.sum()
        out, err = capfd.readouterr()

        assert out == "aからbまでの総和を求めます。\n整数a:整数b:3から8までの総和は33です。\n"
        assert err == ""

    def test_sum_verbose1(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("3\n3\n"))
        sut.sum_verbose1()
        out, err = capfd.readouterr()

        assert out == "aからbまでの総和を求めます。\n整数a:整数b:3 = 3\n"
        assert err == ""

        monkeypatch.setattr("sys.stdin", io.StringIO("3\n4\n"))
        sut.sum_verbose1()
        out, err = capfd.readouterr()

        assert out == "aからbまでの総和を求めます。\n整数a:整数b:3 + 4 = 7\n"
        assert err == ""

        monkeypatch.setattr("sys.stdin", io.StringIO("3\n7\n"))
        sut.sum_verbose1()
        out, err = capfd.readouterr()

        assert out == "aからbまでの総和を求めます。\n整数a:整数b:3 + 4 + 5 + 6 + 7 = 25\n"
        assert err == ""
