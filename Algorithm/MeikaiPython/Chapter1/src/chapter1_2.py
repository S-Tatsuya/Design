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
