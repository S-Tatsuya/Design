import io

import src.chapter3_2 as sut


class TestChapter3_2:
    def test_ssearch_for(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("7\n6\n4\n3\n2\n1\n2\n8\n2\n"))
        sut.ssearch_for()
        out, err = capfd.readouterr()
        assert out == "要素数:x[0]:x[1]:x[2]:x[3]:x[4]:x[5]:x[6]:探す値:それはx[3]にあります。\n"
        assert err == ""

    def test_seq_search(self):
        datas = [12.7, 3.14, 6.4, 7.2]
        key = 6.4
        result = sut.seq_search(datas, key)
        assert result == 2

        t = (4, 7, 5.6, 2, 3.14, 1)
        key = 5.6
        result = sut.seq_search(t, key)
        assert result == 2
        s = "string"
        key = "n"
        result = sut.seq_search(s, key)
        assert result == 4
        a = ["DTS", "AAC", "FLAC"]
        key = "DTS"
        result = sut.seq_search(a, key)
        assert result == 0
