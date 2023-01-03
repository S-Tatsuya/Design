# import pytest
from src.MountainBike import MountainBike
from src.RoadBike import RoadBike
from src.RecumbentBike import RecumbentBike


def test_bicycle():
    sut = RoadBike(size="M", tape_color="red")

    assert sut.size == "M"
    assert sut.tire_size == "23"
    assert sut.chain == "10-speed"
    assert sut.spares == {"tire_size": "23", "chain": "10-speed", "tape_color": "red"}


def test_mountain():
    sut = MountainBike(
        style="mountain", size="S", front_shock="Manitou", rear_shock="Fox"
    )

    assert sut.size == "S"
    assert sut.tire_size == "2.1"
    assert sut.chain == "10-speed"
    assert sut.spares == {"tire_size": "2.1", "chain": "10-speed", "rear_shock": "Fox"}


def test_RecumbentBike():
    sut = RecumbentBike(flag="tall and orange")

    assert sut.spares == {
        "tire_size": "28",
        "chain": "9-speed",
        "flag": "tall and orange",
    }


# def test_RecumbentBike():
#     with pytest.raises(TypeError):
#         _ = RecumbentBike()


# @abstractmethodを使用しない場合にエラーを検出する方法
# def test_exception():
#     with pytest.raises(NotImplementedError) as e:
#         sut = RecumbentBike()
#         _ = sut
#
#     assert str(e.value) == "This RecumbentBie cannot respond to:"
