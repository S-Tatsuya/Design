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
    n = int(input("nの値:"))

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
