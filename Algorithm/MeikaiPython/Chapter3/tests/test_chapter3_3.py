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

    def test_bsearch_verbose(self, capfd):
        datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        result = sut.bsearch_verbose(datas, 8)
        out, err = capfd.readouterr()
        assert result == 7
        assert out == (
            "   |   0   1   2   3   4   5   6   7   8   9  10\n"
            "---+----------------------------------------------\n"
            "   | <-                    +                  ->\n"
            "  5|   1   2   3   4   5   6   7   8   9  10  11\n"
            "   |\n"
            "   |                         <-        +      ->\n"
            "  8|   1   2   3   4   5   6   7   8   9  10  11\n"
            "   |\n"
            "   |                         <+  ->\n"
            "  6|   1   2   3   4   5   6   7   8   9  10  11\n"
            "   |\n"
            "   |                             <+->\n"
            "  7|   1   2   3   4   5   6   7   8   9  10  11\n"
            "   |\n"
        )
        assert err == ""
