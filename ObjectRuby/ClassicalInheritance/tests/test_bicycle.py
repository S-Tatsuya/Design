from src.Bicycle import Bicycle


def test_bicycle_road():
    sut = Bicycle(size="M", tape_color="red")

    assert sut.size == "M"
    assert sut.spares == {"tire_size": "23", "chain": "10-speed", "tape_color": "red"}


def test_bicycle_mountain():
    sut = Bicycle(style="mountain", size="S", front_shock="Manitou", rear_shock="Fox")

    assert sut.spares == {"tire_size": "2.1", "chain": "10-speed", "rear_shock": "Fox"}
