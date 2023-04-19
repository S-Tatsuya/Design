import datetime
from src.Bicycle import Bicycle
from src.Vehicle import Vehicle
from src.Mechanic import Mechanic
from src.Schedule import Schedule


def test_bicycle(capfd):
    sut = Bicycle()
    starting = datetime.date(2015, 9, 4)
    ending = datetime.date(2015, 9, 10)
    assert sut.is_schedulable(starting, ending) is False

    out, err = capfd.readouterr()
    assert out == "This Bicycle is not scheduled\nbetween 2015-09-03 and 2015-09-10.\n"
    assert err == ""


def test_vehicle(capfd):
    sut = Vehicle()
    starting = datetime.date(2015, 9, 4)
    ending = datetime.date(2015, 9, 10)
    assert sut.is_schedulable(starting, ending) is False

    out, err = capfd.readouterr()
    assert out == "This Vehicle is not scheduled\nbetween 2015-09-01 and 2015-09-10.\n"
    assert err == ""


def test_mechanic(capfd):
    sut = Mechanic()
    starting = datetime.date(2015, 9, 4)
    ending = datetime.date(2015, 9, 10)
    assert sut.is_schedulable(starting, ending) is False

    out, err = capfd.readouterr()
    assert out == "This Mechanic is not scheduled\nbetween 2015-08-31 and 2015-09-10.\n"
    assert err == ""


def test_schedule(capfd):
    sut = Schedule()
    target = Bicycle()
    starting = datetime.date(2015, 9, 4)
    ending = datetime.date(2015, 9, 10)
    assert sut.is_schedulable(target, starting, ending) is False

    out, err = capfd.readouterr()
    assert out == "This Bicycle is not scheduled\nbetween 2015-09-04 and 2015-09-10.\n"
    assert err == ""
