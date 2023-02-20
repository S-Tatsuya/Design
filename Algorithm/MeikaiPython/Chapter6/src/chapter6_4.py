from typing import MutableSequence, Any
from collections import deque


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


def insertion_sort(datas: MutableSequence) -> MutableSequence:
    result = datas
    n = len(result)
    for i in range(1, n):
        j = i
        tmp = result[i]
        while j > 0 and result[j - 1] > tmp:
            result[j] = result[j - 1]
            j -= 1
        result[j] = tmp
    return result


def binary_insertion_sort(datas: MutableSequence) -> MutableSequence:
    result = datas
    n = len(result)
    for i in range(1, n):
        key = result[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2
            if result[pc] == key:
                break
            elif result[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            result[j] = result[j - 1]
        result[pd] = key
    return result


def shell_sort(datas: MutableSequence) -> MutableSequence:
    result = datas
    n = len(result)
    h = 1
    while h < n // 9:
        h = h * 3 + 1
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = result[i]
            while j >= 0 and result[j] > tmp:
                result[j + h] = result[j]
                j -= h
            result[j + h] = tmp
        h //= 3

    return result


def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n // 2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f"枢軸の値は{x}です。")
    print("枢軸以下のグループ")
    print(*a[0:pl])

    if pl > pr + 1:
        print("枢軸と一致するグループ")
        print(*a[pr + 1 : pl])

    print("枢軸以上のグループ")
    print(*a[pr + 1 : n])


def quick_sort(a: MutableSequence, left: int, right: int) -> None:
    range_stack = Stack(right - left + 1)
    range_stack.push((left, right))

    while not range_stack.is_empty():
        pl, pr = left, right = range_stack.pop()
        x = a[(left + right) // 2]

        while pl <= pr:
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr:
            range_stack.push((left, pr))
        if pl < right:
            range_stack.push((pl, right))
