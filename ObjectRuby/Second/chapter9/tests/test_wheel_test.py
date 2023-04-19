import pytest
from abc import ABCMeta, abstractmethod

from src.wheel import Wheel, Gear


class DiameterizableInterfaceTest(metaclass=ABCMeta):
    @abstractmethod
    def set_up(self):
        self.diameter = None

    def test_implements_the_diameterizable_interface(self):
        assert hasattr(self.diameter, "width")
        assert callable(getattr(self.diameter, "width"))


class TestWheel(DiameterizableInterfaceTest):
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.diameter = Wheel(26, 1.5)

    def test_calculates_diameter(self):
        self.sut = Wheel(26, 1.5)
        assert self.sut.width() == 29


class TestGear(DiameterizableInterfaceTest):
    def set_up(self, mocker):
        self.diameter = mocker.Mock()
        self.diameter.diameter.return_value = 10

    def test_calculates_gear_inches(self):
        gear = Gear(chainring=52, cog=11, wheel=self.diameter)
        assert gear.gear_inches == pytest.approx(47.27, abs=0.01)

    def test_notifies_observers_when_cogs_change(self, mocker):
        observerMock = mocker.Mock()
        gear = Gear(chainring=52, cog=11, observer=observerMock)
        gear.cog = 27
        observerMock.changed.assert_called_with(52, 27)

    def test_notifies_observers_when_chainrings_change(self, mocker):
        observerMock = mocker.Mock()
        gear = Gear(chainring=52, cog=11, observer=observerMock)
        gear.chainring = 30
        observerMock.changed.assert_called_with(30, 11)
