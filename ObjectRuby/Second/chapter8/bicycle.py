from parts_factory import PartsFactory


class Bicycle:
    def __init__(self, **kwargs):
        self._size = kwargs.get("size", None)
        self._parts = kwargs.get("parts", None)

    @property
    def size(self):
        return self._size

    @property
    def parts(self):
        return self._parts

    def spares(self):
        return self.parts.spares()  # type: ignore


if __name__ == "__main__":
    road_bike = Bicycle(size="M", parts=PartsFactory.build(PartsFactory.road_config))
    spares = road_bike.spares()
    for spare in spares:
        print(vars(spare))

    mountain_bike = Bicycle(
        size="L", parts=PartsFactory.build(PartsFactory.mountain_parts)
    )
    spares = road_bike.spares()
    for spare in spares:
        print(vars(spare))

    recumbent_bike = Bicycle(
        size="L", parts=PartsFactory.build(PartsFactory.recumbent_config)
    )
    spares = road_bike.spares()
    for spare in spares:
        print(vars(spare))
