from __future__ import annotations
from typing import Any, Optional
import hashlib
from enum import Enum


class Node:
    def __init__(self, key: Any, value: Any, next: Optional[Node]):
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table: list[Optional[Node]] = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self):
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end="")
            while p is not None:
                print(f" → {p.key}（{p.value}）", end="")
                p = p.next
            print()


Menu = Enum("Menu", ["追加", "削除", "探索", "ダンプ", "終了"])


def _select_memu():
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep=" ", end="")
        n = int(input(":"))
        if 1 <= n <= len(Menu):
            return Menu(n)


def chained_bash_test():
    hash = ChainedHash(13)
    while True:
        menu = _select_memu()

        if menu == Menu.追加:
            key = int(input("キー:"))
            val = input("値:")
            if not hash.add(key, val):
                print("追加失敗!")

        elif menu == Menu.削除:
            key = int(input("キー:"))
            if not hash.remove(key):
                print("追加失敗!")

        elif menu == Menu.探索:
            key = int(input("キー:"))
            t = hash.search(key)
            if t is not None:
                print(f"そのキーを持つ値は{t}です。")
            else:
                print("該当するデータはありません。")

        elif menu == Menu.ダンプ:
            hash.dump()

        else:
            break
