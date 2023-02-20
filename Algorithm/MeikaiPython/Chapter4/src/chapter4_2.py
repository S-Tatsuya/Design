from typing import Any


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 10):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, x: Any):
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = x
        self.rear += 1
        self.no += 1

        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        result = self.que[self.front]
        self.front += 1
        self.no -= 1

        if self.front == self.capacity:
            self.front = 0
        return result

    def peek(self) -> Any:
        return self.que[self.front]

    def find(self, value: Any) -> int:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value) -> int:
        counter = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                counter += 1

        return counter

    def __contains__(self, value: Any) -> bool:
        return bool(self.count(value))

    def clear(self):
        self.no = self.front = self.rear = 0

    def dump(self):
        if self.is_empty():
            print("キューは空です。")
        else:
            for i in range(self.no):
                print(self.que[i + self.front % self.capacity], end=" ")
            print()
