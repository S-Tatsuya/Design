# import pytest
from src.Bicycle import Bicycle
from src.PartsFactory import PartsFactory


def test_bicycle():
    config = [["chain", "10-speed"], ["tire_size", "23"], ["tape_color", "red"]]
    sut_road = PartsFactory.build(config)

    sut = Bicycle(size="M", parts=sut_road)

    assert sut.size == "M"
    assert sut.spares == {"tire_size": "23", "chain": "10-speed", "tape_color": "red"}
    assert sut.parts == [
        ("chain", "10-speed", True),
        ("tire_size", "23", True),
        ("tape_color", "red", True),
    ]


def test_mountain():
    config = [
        ["chain", "10-speed"],
        ["tire_size", "2.1"],
        ["rear_shock", "Fox"],
        ["front_shock", "Manitou", False],
    ]
    sut_mountain = PartsFactory.build(config)
    sut = Bicycle(style="mountain", size="S", parts=sut_mountain)

    assert sut.size == "S"
    assert sut.spares == {"tire_size": "2.1", "chain": "10-speed", "rear_shock": "Fox"}
    assert sut.parts == [
        ("chain", "10-speed", True),
        ("tire_size", "2.1", True),
        ("rear_shock", "Fox", True),
        ("front_shock", "Manitou", False),
    ]


def test_RecumbentBike():
    config = [["chain", "9-speed"], ["tire_size", "28"], ["flag", "tall and orange"]]
    sut_recumbernt = PartsFactory.build(config)
    sut = Bicycle(parts=sut_recumbernt)

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
    config = [["chain", "10-speed"], ["tire_size", "23"], ["tape_color", "red"]]
    sut_road = PartsFactory.build(config)

    assert sut_road.spares == {
        "tire_size": "23",
        "chain": "10-speed",
        "tape_color": "red",
    }

    config = [
        ["chain", "10-speed"],
        ["tire_size", "2.1"],
        ["rear_shock", "Fox"],
        ["front_shock", "Manitou", False],
    ]
    sut_mountain = PartsFactory.build(config)

    assert sut_mountain.spares == {
        "tire_size": "2.1",
        "chain": "10-speed",
        "rear_shock": "Fox",
    }

    config = [["chain", "9-speed"], ["tire_size", "28"], ["flag", "tall and orange"]]
    sut_recumbernt = PartsFactory.build(config)

    assert sut_recumbernt.spares == {
        "tire_size": "28",
        "chain": "9-speed",
        "flag": "tall and orange",
    }


def test_parts_factory():
    config = [["chain", "10-speed"], ["tire_size", "23"], ["tape_color", "red"]]
    sut_road = PartsFactory.build(config)

    assert sut_road.spares == {
        "tire_size": "23",
        "chain": "10-speed",
        "tape_color": "red",
    }

    config = [
        ["chain", "10-speed"],
        ["tire_size", "2.1"],
        ["rear_shock", "Fox"],
        ["front_shock", "Manitou", False],
    ]
    sut_mountain = PartsFactory.build(config)
    assert sut_mountain.spares == {
        "tire_size": "2.1",
        "chain": "10-speed",
        "rear_shock": "Fox",
    }

    config = [["chain", "9-speed"], ["tire_size", "28"], ["flag", "tall and orange"]]
    sut_recumbernt = PartsFactory.build(config)

    assert sut_recumbernt.spares == {
        "tire_size": "28",
        "chain": "9-speed",
        "flag": "tall and orange",
    }
