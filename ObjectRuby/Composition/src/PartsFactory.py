from src.Parts import Parts
from src.Part import Part

_ = Parts
_ = Part


class PartsFactory:
    @classmethod
    def build(cls, configs, part_class="Part", parts_class="Parts"):
        return eval(parts_class)(
            [
                eval(part_class)(
                    name=config[0],
                    description=config[1],
                    needs_spare=next(iter(config[2:]), True),
                )
                for config in configs
            ]
        )
