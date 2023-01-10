import pytest

from src.Gear import Gear


class DiameterDouble:
    def diameter(self):
        return 10


def test_calculates_gear_inches():
    sut = Gear(chainring=52, cog=11, wheel=DiameterDouble())

    assert pytest.approx(sut.gear_inches(), 0.01) == 47.27
