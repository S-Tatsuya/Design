from collections import defaultdict
from dataclasses import dataclass

from parts import Parts, RoadBikeParts, MountainBikeParts  # pyright: ignore # noqa


class PartsFactory:
    @classmethod
    def build(cls, config):
        temp_parts = []
        for part_info in config:
            part_config = defaultdict(lambda: True, enumerate(part_info))
            temp_part = PartsFactory.Part(
                name=part_config[0],  # type: ignore
                description=part_config[1],  # type: ignore
                needs_spare=part_config[2],
            )
            temp_parts.append(temp_part)

        return Parts(temp_parts)

    @dataclass
    class Part:
        name: str
        description: str
        needs_spare: bool = True

    road_config = [["chain", "10-speed"], ["tire_size", "23"], ["tape_color", "red"]]

    mountain_parts = [
        ["chain", "10-speed"],
        ["tire_size", "2.1"],
        ["front_shock", "Manitou", False],
        ["rear_shock", "Fox"],
    ]

    recumbent_config = [
        ["chain", "9-speed"],
        ["tire_size", "28"],
        ["flag", "tall and orange"],
    ]


if __name__ == "__main__":
    parts = PartsFactory.build(config=PartsFactory.road_config)
    for part in parts:
        print(vars(part))

    parts = PartsFactory.build(config=PartsFactory.mountain_parts)
    for part in parts:
        print(vars(part))
