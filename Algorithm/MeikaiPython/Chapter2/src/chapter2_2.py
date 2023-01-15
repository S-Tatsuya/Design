from typing import Any, Sequence


def max():
    print("配列の最大値を求めます。")
    num = int(input("要素数:"))
    x = []

    for i in range(num):
        x.append(int(input(f"x[{i}]:")))

    print(f"最大値は{_max_of(x)}です。")


def _max_of(datas: Sequence) -> Any:
    """シーケンスdatasの要素の最大値を返却する"""
    maximum = datas[0]
    for data in datas:
        if data > maximum:
            maximum = data
    return maximum
