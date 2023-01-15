import io

import src.chapter2_2 as sut


class TestChapter2_2:
    def test_max(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("5\n172\n153\n192\n140\n165\n"))
        sut.max()
        out, err = capfd.readouterr()
        assert out == "配列の最大値を求めます。\n要素数:x[0]:x[1]:x[2]:x[3]:x[4]:最大値は192です。\n"
        assert err == ""
