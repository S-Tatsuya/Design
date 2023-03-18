from src.Parts import Parts

_ = Parts


class PartsFactory:
    @staticmethod
    def build(configs, part_class="PartsFactory.Part", parts_class="Parts"):
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

    class Part:
        def __init__(self, **kwargs):
            self._name = kwargs.get("name")
            self._description = kwargs.get("description")
            self._needs_spare = kwargs.get("needs_spare")

        @property
        def name(self):
            return self._name

        @property
        def description(self):
            return self._description

        @property
        def needs_spare(self):
            return self._needs_spare
