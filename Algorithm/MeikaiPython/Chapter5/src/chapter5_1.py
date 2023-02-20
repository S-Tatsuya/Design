def factorial(value: int) -> int:
    if value < 0:
        raise ValueError("負の数は受け付けません")

    if value <= 0:
        return 1

    return value * factorial(value - 1)


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a

    return gcd(b, a % b)
