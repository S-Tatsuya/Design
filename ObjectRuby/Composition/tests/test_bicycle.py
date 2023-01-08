# import pytest
from src.MountainBike import MountainBike
from src.RoadBike import RoadBike
from src.RecumbentBike import RecumbentBike
from src.Parts import RoadBikeParts, MountainBikeParts, RecumbentBikeParts


def test_bicycle():
    sut = RoadBike(size="M", parts=RoadBikeParts(tape_color="red"))

    assert sut.size == "M"
    assert sut.spares == {"tire_size": "23", "chain": "10-speed", "tape_color": "red"}


def test_mountain():
    sut = MountainBike(
        style="mountain",
        size="S",
        parts=MountainBikeParts(front_shock="Manitou", rear_shock="Fox"),
    )

    assert sut.size == "S"
    assert sut.spares == {"tire_size": "2.1", "chain": "10-speed", "rear_shock": "Fox"}


def test_RecumbentBike():
    sut = RecumbentBike(parts=RecumbentBikeParts(flag="tall and orange"))

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


def test_parts():
    sut_road = RoadBikeParts(tape_color="red")

    assert sut_road.chain == "10-speed"
    assert sut_road.tire_size == "23"
    assert sut_road.spares == {
        "tire_size": "23",
        "chain": "10-speed",
        "tape_color": "red",
    }

    sut_mountain = MountainBikeParts(front_shock="Maintou", rear_shock="Fox")
    assert sut_mountain.tire_size == "2.1"
    assert sut_mountain.chain == "10-speed"
    assert sut_mountain.spares == {
        "tire_size": "2.1",
        "chain": "10-speed",
        "rear_shock": "Fox",
    }

    sut_recumbernt = RecumbentBikeParts(flag="tall and orange")

    assert sut_recumbernt.spares == {
        "tire_size": "28",
        "chain": "9-speed",
        "flag": "tall and orange",
    }
