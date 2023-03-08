from src.money import Money


class Bank:
    def reduce(self, source, to):
        if isinstance(source, Money):
            return source.reduce(to)
        sum = source
        return sum.reduce(to)
