from src.Bicycle import Bicycle
from src.MountainBike import MountainBike


def test_bicycle():
    sut = Bicycle(size="M", tape_color="red")

    assert sut.size == "M"
    assert sut.spares == {"tire_size": "23", "chain": "10-speed", "tape_color": "red"}


def test_mountain():
    sut = MountainBike(
        style="mountain", size="S", front_shock="Manitou", rea_shock="Fox"
    )

    assert sut.size == "S"
    assert sut.spares == {"tire_size": "2.1", "chain": "10-speed", "rear_shock": "Fox"}
