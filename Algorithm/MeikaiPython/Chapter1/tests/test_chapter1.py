import io

import src.chapter1 as chapter1


class TestChapter1:
    def test_max3(self, monkeypatch, capfd):
        monkeypatch.setattr("sys.stdin", io.StringIO("1\n2\n3"))

        chapter1.max3()

        out, err = capfd.readouterr()
        assert out == "三つの整数の最大値を求めます。\n整数aの値:整数bの値:整数cの値:最大値は3です。\n"
        assert err == ""

    def test_max3_func(self):
        assert chapter1.max3_func(3, 2, 1) == 3
        assert chapter1.max3_func(3, 2, 2) == 3
        assert chapter1.max3_func(3, 1, 2) == 3
        assert chapter1.max3_func(3, 2, 3) == 3
        assert chapter1.max3_func(2, 1, 3) == 3
        assert chapter1.max3_func(3, 3, 2) == 3
        assert chapter1.max3_func(3, 3, 3) == 3
        assert chapter1.max3_func(2, 2, 3) == 3
        assert chapter1.max3_func(2, 3, 1) == 3
        assert chapter1.max3_func(2, 3, 2) == 3
        assert chapter1.max3_func(1, 3, 2) == 3
        assert chapter1.max3_func(2, 3, 3) == 3
        assert chapter1.max3_func(1, 2, 3) == 3
