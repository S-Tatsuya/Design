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

    def test_skip(self, capfd):
        sut.skip()
        out, err = capfd.readouterr()
        assert out == "1 2 3 4 5 6 7 9 10 11 12 \n"
        assert err == ""

    def test_digits1(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("9\n146\n57\n"))
        sut.digits1()
        out, err = capfd.readouterr()
        assert out == "2桁の整数値を入力してください。\n値は:値は:値は:読み込んだのは57です。\n"
        assert err == ""

    def test_multiplication_tabel(self, capfd):
        sut.multiplication_table()
        out, err = capfd.readouterr()
        assert out == (
            "---------------------------\n"
            "  1  2  3  4  5  6  7  8  9\n"
            "  2  4  6  8 10 12 14 16 18\n"
            "  3  6  9 12 15 18 21 24 27\n"
            "  4  8 12 16 20 24 28 32 36\n"
            "  5 10 15 20 25 30 35 40 45\n"
            "  6 12 18 24 30 36 42 48 54\n"
            "  7 14 21 28 35 42 49 56 63\n"
            "  8 16 24 32 40 48 56 64 72\n"
            "  9 18 27 36 45 54 63 72 81\n"
            "---------------------------\n"
        )
        assert err == ""

    def test_triangle_lb(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
        sut.trianle_lb()
        out, err = capfd.readouterr()
        assert out == "左下直角の二等辺三角形\n短辺の長さ:*\n**\n***\n****\n*****\n"
        assert err == ""

    def test_triangle_rb(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
        sut.trianle_rb()
        out, err = capfd.readouterr()
        assert out == "右下直角の二等辺三角形\n短辺の長さ:    *\n   **\n  ***\n ****\n*****\n"
        assert err == ""
