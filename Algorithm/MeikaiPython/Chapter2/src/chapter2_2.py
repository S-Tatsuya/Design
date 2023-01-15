import random

from typing import Any, Sequence


def max():
    print("配列の最大値を求めます。")
    num = int(input("要素数:"))
    x = []

    for i in range(num):
        x.append(int(input(f"x[{i}]:")))

    print(f"最大値は{_max_of(x)}です。")


def max_of_test_input():
    print("配列の最大値を求めます。")
    print("注:'End'で入力終了。")
    x = []
    number = 0

    while True:
        s = input(f"x[{number}]:")
        if s == "End":
            break

        x.append(int(s))
        number += 1

    print(f"{number}個読み込みました。")
    print(f"最大値は{_max_of(x)}です。")


def max_of_test_randint(seed=None):
    print("乱数の最大値を求めます。")
    num = int(input("乱数の個数:"))
    lo = int(input("乱数の下限:"))
    hi = int(input("乱数の上限:"))
    x = []

    for i in range(num):
        random.seed() if seed is None else random.seed(i + seed)
        x.append(random.randint(lo, hi))

    print(f"{x}")
    print(f"最大値は{_max_of(x)}です。")


def max_of_test():
    t = (4, 7, 5.6, 2, 3.14, 1)
    s = "string"
    a = ["DTS", "AAC", "FLAC"]

    print(f"{t}の最大値は{_max_of(t)}です。")
    print(f"{s}の最大値は{_max_of(s)}です。")
    print(f"{a}の最大値は{_max_of(a)}です。")


def _max_of(datas: Sequence) -> Any:
    """シーケンスdatasの要素の最大値を返却する"""
    maximum = datas[0]
    for data in datas:
        if data > maximum:
            maximum = data
    return maximum
