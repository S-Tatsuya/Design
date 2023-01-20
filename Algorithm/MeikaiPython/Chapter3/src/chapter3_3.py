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


def bsearch_verbose(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    print("   |", end="")
    for i in range(len(a)):
        print(f"{i:4}", end="")
    print("")
    print("---+" + (4 * len(a) + 2) * "-")

    while True:
        pc = (pl + pr) // 2

        print("   |", end="")
        if pl != pc:
            print((pl * 4 + 1) * " " + "<-" + ((pc - pl) * 4) * " " + "+", end="")
        else:
            print((pc * 4 + 1) * " " + "<+", end="")

        if pc != pr:
            print(((pr - pc) * 4 - 2) * " " + "->")
        else:
            print("->")
        print(f"{pc:3}|", end="")

        for i in range(len(a)):
            print(f"{a[i]:4}", end="")
        print("\n   |")

        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            break

    return -1
