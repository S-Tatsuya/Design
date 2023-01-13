def max3():
    print("三つの整数の最大値を求めます。")
    a = int(input("整数aの値:"))
    b = int(input("整数bの値:"))
    c = int(input("整数cの値:"))

    maximum = a
    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c

    print(f"最大値は{maximum}です。")


def max3_func(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c

    return maximum


def med3_func(a, b, c):
    if a >= b:  # ここに`=`が必要なことに気づけ無い
        if b >= c:
            return b

        if a <= c:
            return a

        return c

    if a > c:
        return a

    if b > c:
        return c

    return b


def judge_sign():
    n = int(input("整数:"))

    if n > 0:
        print("その値は正です。")
        return

    if n < 0:
        print("その値は負です。")
        return

    print("その値は0です。")


def branch1():
    n = int(input("整数:"))

    if n == 1:
        print("A")
        return

    if n == 2:
        print("B")
        return

    print("C")


def branch2():
    n = int(input("整数:"))

    if n == 1:
        print("A")
        return

    if n == 2:
        print("B")
        return

    if n == 3:
        print("C")
        return

    print("")
