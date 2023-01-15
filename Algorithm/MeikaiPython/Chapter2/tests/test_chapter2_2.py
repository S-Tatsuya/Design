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

    def test_max_of_test(self, capfd):
        sut.max_of_test()
        out, err = capfd.readouterr()
        assert out == (
            "(4, 7, 5.6, 2, 3.14, 1)の最大値は7です。\n"
            "stringの最大値はtです。\n"
            "['DTS', 'AAC', 'FLAC']の最大値はFLACです。\n"
        )
        assert err == ""
