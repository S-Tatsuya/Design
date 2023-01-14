import random


def sum1ton_while():
    print("1からnまでの総和を求めます。")
    n = int(input("nの値:"))

    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1

    print(f"1から{n}までの総和は{sum}です。")


def sum1ton_for():
    print("1からnまでの総和を求めます。")

    while True:
        n = int(input("nの値:"))
        if n > 0:
            break

    sum = 0
    for i in range(1, n + 1):
        sum += i

    print(f"1から{n}までの総和は{sum}です。")


def sum_gauss():
    print("1からnまでの総和を求めます。")
    n = int(input("nの値:"))

    # `//`演算子を使うことでint型の戻り値になる
    sum = n * (n + 1) // 2

    print(f"1から{n}までの総和は{sum}です。")


def sum():
    print("aからbまでの総和を求めます。")
    a = int(input("整数a:"))
    b = int(input("整数b:"))

    if a > b:
        a, b = b, a

    sum = 0
    for i in range(a, b + 1):
        sum += i

    print(f"{a}から{b}までの総和は{sum}です。")


def sum_verbose1():
    print("aからbまでの総和を求めます。")
    a = int(input("整数a:"))
    b = int(input("整数b:"))

    if a > b:
        a, b = b, a

    sum = 0
    for i in range(a, b):
        print(f"{i} + ", end="")
        sum += i

    print(f"{b} = ", end="")
    sum += b
    print(sum)


def alternative1():
    print("記号文字+と-を交互に表示します。")
    n = int(input("全部で何個:"))

    for _ in range(n // 2):
        print("+-", end="")

    if n % 2:
        print("+", end="")

    print()


def print_stars1():
    print("記号文字*を表示します。")
    n = int(input("全部で何個:"))
    w = int(input("何個ごとに改行:"))

    for _ in range(n // w):
        print("*" * w)

    rest = n % w
    if rest:
        print("*" * rest)


def rectangle():
    area = int(input("面積は:"))

    for i in range(1, area + 1):
        if i * i > area:
            break

        if area % i:
            continue
        print(f"{i} × {area // i}")


def for_else(seed=None):
    n = int(input("乱数は何個:"))

    for i in range(n):
        random.seed() if seed is None else random.seed(i + seed)
        r = random.randint(10, 99)
        print(r, end=" ")
        if r == 47:
            print("\n事情により中断します。")
            break
    else:
        print("\n乱数生成終了")


def skip():
    for i in list(range(1, 8)) + list(range(9, 13)):
        print(i, end=" ")

    print()


def digits1():
    print("2桁の整数値を入力してください。")
    while True:
        no = int(input("値は:"))
        if 10 <= no <= 99:
            break
    print(f"読み込んだのは{no}です。")


def multiplication_table():
    print("-" * 27)
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i * j:3}", end="")
        print()
    print("-" * 27)


def trianle_lb():
    print("左下直角の二等辺三角形")
    n = int(input("短編の長さ:"))

    for i in range(n):
        for _ in range(i + 1):
            print("*", end="")

        print()


def trianle_rb():
    print("右下直角の二等辺三角形")
    n = int(input("短辺の長さ:"))

    for i in range(n):
        for _ in range(n - i - 1):
            print(" ", end="")
        for _ in range(i + 1):
            print("*", end="")
        print()
