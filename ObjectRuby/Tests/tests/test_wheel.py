from src.Wheel import Wheel


def test_wheel():
    sut = Wheel(26, 1.5)

    assert sut.diameter() == 29
