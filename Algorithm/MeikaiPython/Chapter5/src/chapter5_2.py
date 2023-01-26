from collections import deque
from typing import Any


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


def recur1(n: int):
    if n > 0:
        recur1(n - 1)
        print(n)
        recur1(n - 2)


def recur(n: int):
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2


def recur1b(n: int):
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break
