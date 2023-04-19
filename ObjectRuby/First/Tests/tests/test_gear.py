import pytest

from src.Gear import Gear
from src.Observer import Observer


class DiameterDouble:
    def diameter(self):
        return 10


class TestGear:
    @pytest.fixture
    def setup_observer_mock(self, mocker):
        self.observer_mock = mocker.Mock(spec=Observer)
        self.sut = Gear(
            chainring=52, cog=11, wheel=DiameterDouble(), observer=self.observer_mock
        )

    def test_calculates_gear_inches(self):
        sut = Gear(chainring=52, cog=11, wheel=DiameterDouble())

        assert pytest.approx(sut.gear_inches(), 0.01) == 47.27

    def test_notifies_observers_when_cogs_change(self, setup_observer_mock):
        _ = setup_observer_mock
        self.sut.cog = 27
        self.observer_mock.changed.assert_called_once_with(52, 27)

    def test_notifies_observers_when_chainrings_change(self, setup_observer_mock):
        _ = setup_observer_mock
        self.sut.chainring = 42
        self.observer_mock.changed.assert_called_once_with(42, 11)
