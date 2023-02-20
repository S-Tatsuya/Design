from typing import Any, Sequence


def ssearch_for():
    num = int(input("要素数:"))
    x = []
    for i in range(num):
        x.append(int(input(f"x[{i}]:")))
    key = int(input("探す値:"))

    idx = seq_search(x, key)

    if idx == -1:
        print("その値は存在しません。")
    else:
        print(f"それはx[{idx}]にあります。")


def seq_search(a: Sequence, key: Any) -> int:
    for i, data in enumerate(a):
        if data == key:
            return i

    return -1
