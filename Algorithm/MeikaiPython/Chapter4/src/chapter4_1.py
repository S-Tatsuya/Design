from typing import Any
from collections import deque


class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def __contains__(self, value: Any) -> bool:
        return bool(self.count(value))

    def push(self, value: Any):
        if self.is_full():
            raise FixedStack.Full

        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty

        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty

        return self.stk[self.ptr - 1]

    def clear(self):
        self.ptr = 0

    def find(self, value: Any) -> int:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i

        return -1

    def count(self, value: Any) -> int:
        counter = 0
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                counter += 1

        return counter

    def dump(self):
        if self.is_empty():
            print("スタックは空です。")
        else:
            print(self.stk[: self.ptr])

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def is_empty(self) -> bool:
        return self.ptr <= 0


class Stack:
    def __init__(self, maxlen: int = 256):
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        return len(self.__stk)

    def is_empty(self) -> bool:
        return not self.__stk

    def is_full(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        self.__stk.append(value)

    def pop(self) -> Any:
        return self.__stk.pop()

    def peek(self) -> Any:
        return self.__stk[-1]

    def clear(self) -> None:
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        return bool(self.count(value))

    def dump(self):
        print(list(self.__stk))
