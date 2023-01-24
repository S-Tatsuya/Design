class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.prt = 0

    def __len__(self) -> int:
        return self.prt
