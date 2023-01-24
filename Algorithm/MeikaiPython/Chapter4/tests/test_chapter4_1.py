from src.chapter4_1 import FixedStack


class TestChapter4_1:
    def test_fixed_stack(self):
        sut = FixedStack()
        assert sut.__len__() == 0
        assert len(sut) == 0
