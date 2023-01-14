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

        monkeypatch.setattr("sys.stdin", io.StringIO("-6\n0\n10\n"))
        sut.sum1ton_for()
        out, err = capfd.readouterr()

        assert out == "1からnまでの総和を求めます。\nnの値:nの値:nの値:1から10までの総和は55です。\n"
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

    def test_alternative1(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("12\n"))
        sut.alternative1()
        out, err = capfd.readouterr()

        assert out == "記号文字+と-を交互に表示します。\n全部で何個:+-+-+-+-+-+-\n"
        assert err == ""

        monkeypatch.setattr("sys.stdin", io.StringIO("13\n"))
        sut.alternative1()
        out, err = capfd.readouterr()

        assert out == "記号文字+と-を交互に表示します。\n全部で何個:+-+-+-+-+-+-+\n"
        assert err == ""

    def test_print_stars1(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("14\n5\n"))
        sut.print_stars1()

        out, err = capfd.readouterr()
        assert out == "記号文字*を表示します。\n全部で何個:何個ごとに改行:*****\n*****\n****\n"
        assert err == ""

    def test_rectanle(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("32\n"))
        sut.rectangle()

        out, err = capfd.readouterr()
        assert out == "面積は:1 × 32\n2 × 16\n4 × 8\n"
        assert err == ""

    def test_for_else(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
        sut.for_else(seed=10)

        out, err = capfd.readouterr()

        assert out == "乱数は何個:83 67 70 43 23 \n乱数生成終了\n"
        assert err == ""

        monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
        sut.for_else(seed=20)

        out, err = capfd.readouterr()

        assert out == "乱数は何個:97 31 27 47 \n事情により中断します。\n"
        assert err == ""
