from src.Wheel import Wheel
from src.Gear import Gear
import math


def test_gear():
    gear = Gear(52, 11)
    result = 52 / 11
    assert math.isclose(result, gear.Ratio)

    result = (52 / 11) * (26 + (1.5 * 2))
    assert math.isclose(result, gear.gearInches(Wheel(26, 1.5).Diameter))

    gear = Gear(52, 11)
    result = 52 / 11
    assert math.isclose(result, gear.Ratio)
    assert math.isclose(0, gear.gearInches(Wheel(0, 0).Diameter))


def test_wheel():
    wheel = Wheel(26, 1.5)
    result = (26 + (1.5 * 2)) * math.pi
    assert math.isclose(result, wheel.Circumference)
