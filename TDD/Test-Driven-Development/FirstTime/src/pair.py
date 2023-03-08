class Pair:
    def __init__(self, base, to):
        self.base = base
        self.to = to

    def __eq__(self, object):
        pair = object
        return self.base == pair.base and self.to == pair.to

    def __hash__(self):
        return 0
