import src.chapter5_3 as sut


class TestChapter5_3:
    def test_hanoi(self, capfd):
        sut.move(3, 1, 3)
        out, err = capfd.readouterr()
        assert out == (
            "円盤[1]を1軸から3軸へ移動\n"
            "円盤[2]を1軸から2軸へ移動\n"
            "円盤[1]を3軸から2軸へ移動\n"
            "円盤[3]を1軸から3軸へ移動\n"
            "円盤[1]を2軸から1軸へ移動\n"
            "円盤[2]を2軸から3軸へ移動\n"
            "円盤[1]を1軸から3軸へ移動\n"
        )
        assert err == ""
