def recur1(n: int):
    if n > 0:
        recur1(n - 1)
        print(n)
        recur1(n - 2)
