def factorial(value: int) -> int:
    if value <= 0:
        return 1

    return value * factorial(value - 1)
