from src.pair import Pair


class Bank:
    def __init__(self):
        self.rates: dict[Pair, int] = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def add_rate(self, base, to, rate):
        self.rates[Pair(base, to)] = rate

    def rate(self, base, to):
        return 1 if base == to else self.rates.get(Pair(base, to))
