import pytest
from abc import ABCMeta, abstractmethod

from src.preparer import Mechanic, TripCoordinator, Driver, Trip


class PrepareInterfaceTest(metaclass=ABCMeta):
    @abstractmethod
    def setUp(self):
        self.sut = None

    def test_implements_interface(self):
        assert hasattr(self.sut, "prepare_trip")
        assert callable(getattr(self.sut, "prepare_trip"))


class TestMechanic(PrepareInterfaceTest):
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.sut = Mechanic()


class TestTripCoordinator(PrepareInterfaceTest):
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.sut = TripCoordinator()


class TestDriver(PrepareInterfaceTest):
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.sut = Driver()


class TestTrip:
    def test_requests_trip_preparation(self, mocker):
        prepareMock = mocker.Mock()
        prepare_mocks = [prepareMock]
        sut = Trip()
        sut.prepare(prepare_mocks)
        prepareMock.prepare_trip.assert_called_with(sut)
