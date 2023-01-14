import io


import src.chapter2_1 as sut


class TestChapter2_1:
    def test_total(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("32\n68\n72\n54\n92\n"))
        sut.total()
        out, err = capfd.readouterr()
        assert out == (
            "5人の点数の合計点と平均点を求めます。\n"
            "1番目の点数:"
            "2番目の点数:"
            "3番目の点数:"
            "4番目の点数:"
            "5番目の点数:"
            "合計は318点です。\n"
            "平均は63.6点です。\n"
        )
        assert err == ""
