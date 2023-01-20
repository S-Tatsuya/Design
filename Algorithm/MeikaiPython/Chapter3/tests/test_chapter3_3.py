import io

import src.chapter3_3 as sut


class TestChapter3_3:
    def test_bsearch(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("7\n1\n2\n3\n5\n7\n8\n9\n5\n"))
        sut.bsearch()
        out, err = capfd.readouterr()
        assert out == (
            "要素数:昇順に入力してください。\nx[0]:x[1]:x[2]:x[3]:x[4]:x[5]:x[6]:探す値:その値はx[3]にあります。\n"
        )
        assert err == ""

        monkeypatch.setattr("sys.stdin", io.StringIO("7\n1\n2\n3\n5\n7\n8\n9\n6\n"))
        sut.bsearch()
        out, err = capfd.readouterr()
        assert out == (
            "要素数:昇順に入力してください。\nx[0]:x[1]:x[2]:x[3]:x[4]:x[5]:x[6]:探す値:その値の要素は存在しません。\n"
        )
        assert err == ""
