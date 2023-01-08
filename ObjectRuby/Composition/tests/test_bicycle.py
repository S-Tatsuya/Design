# import pytest
from src.MountainBike import MountainBike
from src.RoadBike import RoadBike
from src.RecumbentBike import RecumbentBike
from src.Parts import RoadBikeParts, MountainBikeParts, RecumbentBikeParts
from src.Part import Part


def test_bicycle():
    sut_chain = Part(name="chain", description="10-speed")
    sut_tire = Part(name="tire_size", description="23")
    sut_tape = Part(name="tape_color", description="red")
    sut_road = RoadBikeParts([sut_chain, sut_tire, sut_tape])
    sut = RoadBike(size="M", parts=sut_road)

    assert sut.size == "M"
    assert sut.spares == {"tire_size": "23", "chain": "10-speed", "tape_color": "red"}
    assert sut.parts == [
        ("chain", "10-speed", True),
        ("tire_size", "23", True),
        ("tape_color", "red", True),
    ]


def test_mountain():
    sut_chain = Part(name="chain", description="10-speed")
    sut_mountain_tire = Part(name="tire_size", description="2.1")
    sut_rear_shock = Part(name="rear_shock", description="Fox")
    sut_front_shock = Part(name="front_shock", description="Manitou", needs_spare=False)
    sut_mountain = MountainBikeParts(
        [sut_chain, sut_mountain_tire, sut_rear_shock, sut_front_shock]
    )
    sut = MountainBike(style="mountain", size="S", parts=sut_mountain)

    assert sut.size == "S"
    assert sut.spares == {"tire_size": "2.1", "chain": "10-speed", "rear_shock": "Fox"}
    assert sut.parts == [
        ("chain", "10-speed", True),
        ("tire_size", "2.1", True),
        ("rear_shock", "Fox", True),
        ("front_shock", "Manitou", False),
    ]


def test_RecumbentBike():
    sut_recumbernt_chain = Part(name="chain", description="9-speed")
    sut_recumbernt_tire = Part(name="tire_size", description="28")
    sut_flag = Part(name="flag", description="tall and orange")
    sut_recumbernt = RecumbentBikeParts(
        [sut_recumbernt_chain, sut_recumbernt_tire, sut_flag]
    )
    sut = RecumbentBike(parts=sut_recumbernt)

    assert sut.spares == {
        "tire_size": "28",
        "chain": "9-speed",
        "flag": "tall and orange",
    }
    assert sut.parts == [
        ("chain", "9-speed", True),
        ("tire_size", "28", True),
        ("flag", "tall and orange", True),
    ]


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
    sut_chain = Part(name="chain", description="10-speed")
    sut_tire = Part(name="tire_size", description="23")
    sut_tape = Part(name="tape_color", description="red")
    sut_road = RoadBikeParts([sut_chain, sut_tire, sut_tape])

    assert sut_road.spares == {
        "tire_size": "23",
        "chain": "10-speed",
        "tape_color": "red",
    }

    sut_mountain_tire = Part(name="tire_size", description="2.1")
    sut_rear_shock = Part(name="rear_shock", description="Fox")
    sut_front_shock = Part(name="front_shock", description="Manitou", needs_spare=False)
    sut_mountain = MountainBikeParts(
        [sut_chain, sut_mountain_tire, sut_rear_shock, sut_front_shock]
    )
    assert sut_mountain.spares == {
        "tire_size": "2.1",
        "chain": "10-speed",
        "rear_shock": "Fox",
    }

    sut_recumbernt_chain = Part(name="chain", description="9-speed")
    sut_recumbernt_tire = Part(name="tire_size", description="28")
    sut_flag = Part(name="flag", description="tall and orange")
    sut_recumbernt = RecumbentBikeParts(
        [sut_recumbernt_chain, sut_recumbernt_tire, sut_flag]
    )

    assert sut_recumbernt.spares == {
        "tire_size": "28",
        "chain": "9-speed",
        "flag": "tall and orange",
    }


def test_part():
    sut_chain = Part(name="chain", description="10-speed")
    sut_tire = Part(name="tire_size", description="23")
    sut_tape = Part(name="tape_color", description="red")
    sut_mountain_tire = Part(name="tire_size", description="2.1")
    sut_rear_shock = Part(name="rear_shock", description="Fox")
    sut_front_shock = Part(name="front_shock", description="Manitou", needs_spare=False)

    assert sut_chain.name == "chain"
    assert sut_chain.description == "10-speed"
    assert sut_chain.needs_spare is True

    assert sut_tire.name == "tire_size"
    assert sut_tire.description == "23"
    assert sut_tire.needs_spare is True

    assert sut_tape.name == "tape_color"
    assert sut_tape.description == "red"
    assert sut_tape.needs_spare is True

    assert sut_mountain_tire.name == "tire_size"
    assert sut_mountain_tire.description == "2.1"
    assert sut_mountain_tire.needs_spare is True

    assert sut_rear_shock.name == "rear_shock"
    assert sut_rear_shock.description == "Fox"
    assert sut_rear_shock.needs_spare is True

    assert sut_front_shock.name == "front_shock"
    assert sut_front_shock.description == "Manitou"
    assert sut_front_shock.needs_spare is False
