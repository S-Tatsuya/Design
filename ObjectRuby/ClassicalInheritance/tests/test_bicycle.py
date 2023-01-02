from src.Bicycle import Bicycle


def test_bicycle():
    sut = Bicycle(size="M", tape_color="red")

    assert sut.size == "M"
    assert sut.spares == {"tire_size": "23", "chain": "10-speed", "tape_color": "red"}
