from typing import Any, Sequence


def max():
    print("配列の最大値を求めます。")
    num = int(input("要素数:"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]:"))

    print(f"最大値は{_max_of(x)}です。")


def _max_of(a: Sequence) -> Any:
    """シーケンスaの要素の最大値を返却する"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
