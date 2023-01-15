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

    def test_prime1(self, capfd):
        sut.prime1()
        out, err = capfd.readouterr()
        assert out == (
            "2\n"
            "3\n"
            "5\n"
            "7\n"
            "11\n"
            "13\n"
            "17\n"
            "19\n"
            "23\n"
            "29\n"
            "31\n"
            "37\n"
            "41\n"
            "43\n"
            "47\n"
            "53\n"
            "59\n"
            "61\n"
            "67\n"
            "71\n"
            "73\n"
            "79\n"
            "83\n"
            "89\n"
            "97\n"
            "101\n"
            "103\n"
            "107\n"
            "109\n"
            "113\n"
            "127\n"
            "131\n"
            "137\n"
            "139\n"
            "149\n"
            "151\n"
            "157\n"
            "163\n"
            "167\n"
            "173\n"
            "179\n"
            "181\n"
            "191\n"
            "193\n"
            "197\n"
            "199\n"
            "211\n"
            "223\n"
            "227\n"
            "229\n"
            "233\n"
            "239\n"
            "241\n"
            "251\n"
            "257\n"
            "263\n"
            "269\n"
            "271\n"
            "277\n"
            "281\n"
            "283\n"
            "293\n"
            "307\n"
            "311\n"
            "313\n"
            "317\n"
            "331\n"
            "337\n"
            "347\n"
            "349\n"
            "353\n"
            "359\n"
            "367\n"
            "373\n"
            "379\n"
            "383\n"
            "389\n"
            "397\n"
            "401\n"
            "409\n"
            "419\n"
            "421\n"
            "431\n"
            "433\n"
            "439\n"
            "443\n"
            "449\n"
            "457\n"
            "461\n"
            "463\n"
            "467\n"
            "479\n"
            "487\n"
            "491\n"
            "499\n"
            "503\n"
            "509\n"
            "521\n"
            "523\n"
            "541\n"
            "547\n"
            "557\n"
            "563\n"
            "569\n"
            "571\n"
            "577\n"
            "587\n"
            "593\n"
            "599\n"
            "601\n"
            "607\n"
            "613\n"
            "617\n"
            "619\n"
            "631\n"
            "641\n"
            "643\n"
            "647\n"
            "653\n"
            "659\n"
            "661\n"
            "673\n"
            "677\n"
            "683\n"
            "691\n"
            "701\n"
            "709\n"
            "719\n"
            "727\n"
            "733\n"
            "739\n"
            "743\n"
            "751\n"
            "757\n"
            "761\n"
            "769\n"
            "773\n"
            "787\n"
            "797\n"
            "809\n"
            "811\n"
            "821\n"
            "823\n"
            "827\n"
            "829\n"
            "839\n"
            "853\n"
            "857\n"
            "859\n"
            "863\n"
            "877\n"
            "881\n"
            "883\n"
            "887\n"
            "907\n"
            "911\n"
            "919\n"
            "929\n"
            "937\n"
            "941\n"
            "947\n"
            "953\n"
            "967\n"
            "971\n"
            "977\n"
            "983\n"
            "991\n"
            "997\n"
            "除算を行った回数:14622\n"
        )
        assert err == ""
