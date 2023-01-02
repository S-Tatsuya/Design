from src.Trip import Trip
from src.Mechanic import Mechanic
from src.TripCoordinator import TripCoordinator
from src.Driver import Driver
from src.Bicycle import Bicycle
from src.Customer import Customer
from src.Vehicle import Vehicle


def test_ducktyping():
    sut = Trip()
    stub = [Mechanic(), TripCoordinator(), Driver()]
    sut.prepare_ducktyping(stub)
    assert sut.is_ready()


def test_trip():
    sut = Trip()
    stub = [Mechanic()]
    sut.prepare(stub)
    assert sut.is_ready_bicycles()

    sut = Trip()
    stub = [TripCoordinator()]
    sut.prepare(stub)
    assert sut.is_ready_customers()

    sut = Trip()
    stub = [Driver()]
    sut.prepare(stub)
    assert sut.is_ready_vehicle()

    sut = Trip()
    stub = [Mechanic(), TripCoordinator(), Driver()]
    sut.prepare(stub)
    assert sut.is_ready()


def test_mechanic():
    bicycles = [Bicycle(), Bicycle(), Bicycle()]
    sut = Mechanic()
    sut.prepare_bicycles(bicycles)
    assert sut.is_ready(bicycles)


def test_tripcoordinator():
    customers = [Customer(), Customer(), Customer()]
    sut = TripCoordinator()
    sut.buy_foods(customers)
    assert sut.is_ready(customers)


def test_driver():
    vehicle = Vehicle()
    sut = Driver()
    sut.gas_up(vehicle)
    sut.fill_water_tank(vehicle)
    assert sut.is_ready(vehicle)


def test_bicycle():
    sut = Bicycle()
    sut.prepare()
    assert sut.is_ready()


def test_customer():
    sut = Customer()
    sut.prepare()
    assert sut.is_ready()


def test_vehicle():
    sut = Vehicle()
    sut.gas_ready()
    sut.fill_water_tank_ready()
    assert sut.is_ready()
