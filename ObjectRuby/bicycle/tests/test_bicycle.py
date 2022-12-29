from src.Wheel import Wheel
from src.Gear import Gear
import math


def test_gear():
    wheel = Wheel(26, 1.5)
    gear = Gear(52, 11, wheel)
    result = 52 / 11
    assert math.isclose(result, gear.Ratio)

    result = (52 / 11) * wheel.Diameter
    assert math.isclose(result, gear.GearInches)

    gear = Gear(52, 11)
    result = 52 / 11
    assert math.isclose(result, gear.Ratio)
    assert math.isclose(0, gear.GearInches)


def test_wheel():
    wheel = Wheel(26, 1.5)
    result = (26 + (1.5 * 2)) * math.pi
    assert math.isclose(result, wheel.Circumference)
