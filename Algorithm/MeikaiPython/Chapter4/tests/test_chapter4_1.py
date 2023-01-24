import pytest

from src.chapter4_1 import FixedStack


class TestChapter4_1:
    def test_fixed_stack(self):
        sut = FixedStack()
        assert sut.__len__() == 0
        assert len(sut) == 0

        sut.push(1)
        assert sut.__len__() == 1
        assert len(sut) == 1

        assert sut.pop() == 1
        assert sut.__len__() == 0
        assert len(sut) == 0

        sut.push(2)
        sut.push(3)
        assert sut.peek() == 3
        assert len(sut) == 2

        sut.clear()
        assert sut.is_empty()
        assert sut.__len__() == 0

        sut.push(4)
        sut.push(5)
        sut.push(6)

        assert sut.find(5) == 1
        assert sut.find(7) == -1

        sut.push(4)
        sut.push(5)
        sut.push(4)

        assert sut.count(4) == 3
        assert sut.count(7) == 0
        assert 4 in sut
        assert 7 not in sut

    def test_fixed_stack_dump(self, capfd):
        sut = FixedStack()
        sut.push(0)
        sut.push(3)
        sut.push(2)
        sut.push(8)
        sut.push(30)
        sut.push(7)
        sut.push(0)

        sut.dump()
        out, err = capfd.readouterr()
        assert out == "[0, 3, 2, 8, 30, 7, 0]\n"
        assert err == ""

        sut.clear()
        sut.dump()
        out, err = capfd.readouterr()
        assert out == "スタックは空です。\n"
        assert err == ""

    def test_full_exception(self):
        sut = FixedStack(2)

        assert sut.is_full() is False
        assert sut.is_empty()
        sut.push(1)
        sut.push(2)
        assert sut.is_full()
        assert sut.is_empty() is False

        with pytest.raises(FixedStack.Full) as e:
            sut.push(3)

        assert str(e.value) == ""

    def test_empty_exception(self):
        sut = FixedStack()
        assert sut.is_empty()
        with pytest.raises(FixedStack.Empty) as e:
            _ = sut.pop()

        assert str(e.value) == ""

        with pytest.raises(FixedStack.Empty) as e:
            _ = sut.peek()

        assert str(e.value) == ""
