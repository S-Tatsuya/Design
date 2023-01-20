from typing import Sequence, Any


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            break

    return -1


def bsearch():
    num = int(input("要素数:"))
    x = [0] * num

    print("昇順に入力してください。")

    x[0] = int(input("x[0]:"))

    for i in range(1, num):
        while True:
            x[i] = int(input(f"x[{i}]:"))
            if x[i - 1] <= x[i]:
                break

    ky = int(input("探す値:"))

    idx = bin_search(x, ky)

    if idx == -1:
        print("その値の要素は存在しません。")
    else:
        print(f"その値はx[{idx}]にあります。")
