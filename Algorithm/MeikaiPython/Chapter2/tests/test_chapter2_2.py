import io

import src.chapter2_2 as sut


class TestChapter2_2:
    def test_max(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n172\n153\n192\n140\n165\n"))
        sut.max()
        out, err = capfd.readouterr()
        assert out == "配列の最大値を求めます。\n要素数:x[0]:x[1]:x[2]:x[3]:x[4]:最大値は192です。\n"
        assert err == ""

    def test_max_of_test_input(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("15\n72\n64\n7\nEnd\n"))
        sut.max_of_test_input()
        out, err = capfd.readouterr()
        assert (
            out == "配列の最大値を求めます。\n"
            "注:'End'で入力終了。\n"
            "x[0]:"
            "x[1]:"
            "x[2]:"
            "x[3]:"
            "x[4]:"
            "4個読み込みました。\n"
            "最大値は72です。\n"
        )
        assert err == ""

    def test_max_of_test_randint(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n10\n99"))
        sut.max_of_test_randint(10)
        out, err = capfd.readouterr()
        assert (
            out == "乱数の最大値を求めます。\n"
            "乱数の個数:"
            "乱数の下限:"
            "乱数の上限:"
            "[83, 67, 70, 43, 23]\n最大値は83です。\n"
        )
        assert err == ""

    def test_max_of_test(self, capfd):
        sut.max_of_test()
        out, err = capfd.readouterr()
        assert out == (
            "(4, 7, 5.6, 2, 3.14, 1)の最大値は7です。\n"
            "stringの最大値はtです。\n"
            "['DTS', 'AAC', 'FLAC']の最大値はFLACです。\n"
        )
        assert err == ""

    def test_reverse(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("7\n2\n5\n1\n3\n9\n6\n7\n"))
        sut.reverse()
        out, err = capfd.readouterr()
        assert (
            out == "配列の要素の並びを反転します。\n"
            "要素数は:x[0]:x[1]:x[2]:x[3]:x[4]:x[5]:x[6]:"
            "配列の要素の並びを反転しました。\n"
            "x[0] = 7\n"
            "x[1] = 6\n"
            "x[2] = 9\n"
            "x[3] = 3\n"
            "x[4] = 1\n"
            "x[5] = 5\n"
            "x[6] = 2\n"
        )

        assert err == ""

    def test_card_conv(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("29\n2\nN\n"))
        sut.card_conv()
        out, err = capfd.readouterr()
        assert (
            out == "10進数を基数変換します。\n"
            "変換する非負の整数:何進数に変換しますか(2-36):"
            "2進数では11101です。\n"
            "もう一度しますか(Y...はい/N...いいえ):"
        )
        assert err == ""
