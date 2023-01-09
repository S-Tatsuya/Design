import pytest

from src.Gear import Gear
from src.Wheel import Wheel


def test_calculates_gear_inches():
    sut = Gear(chainring=52, cog=11, wheel=Wheel(26, 1.5))

    assert pytest.approx(sut.gear_inches(), 0.1) == 137.1
