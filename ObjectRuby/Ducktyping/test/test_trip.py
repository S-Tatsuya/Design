from src.Trip import Trip
from src.Mechanic import Mechanic
from src.Bicycle import Bicycle


def test_trip():
    sut = Trip()
    stub = Mechanic()
    sut.prepar(stub)
    assert sut.is_ready()


def test_mechanic():
    bicycles = [Bicycle(), Bicycle(), Bicycle()]
    sut = Mechanic()
    sut.prepare_bicycles(bicycles)
    assert sut.is_ready(bicycles)


def test_bicycle():
    sut = Bicycle()
    sut.prepare()
    assert sut.is_ready()
