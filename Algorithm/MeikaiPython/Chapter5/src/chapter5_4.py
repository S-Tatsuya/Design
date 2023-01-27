def queen8_b():
    pos = [0] * 8

    def put() -> None:
        for i in range(8):
            print(f"{pos[i]:2}", end=" ")
        print()

    def set(i: int) -> None:
        for j in range(8):
            pos[i] = j
            if i == 7:
                put()
            else:
                set(i + 1)

    set(0)


def queen8_bb():
    pos = [0] * 8
    flag = [False] * 8

    def put() -> None:
        for i in range(8):
            print(f"{pos[i]:2}", end=" ")
        print()

    def set(i: int) -> None:
        for j in range(8):
            if not flag[j]:
                pos[i] = j
                if i == 7:
                    put()
                else:
                    flag[j] = True
                    set(i + 1)
                    flag[j] = False

    set(0)


def queen8():
    pos = [0] * 8
    flag_a = [False] * 8
    flag_b = [False] * 15
    flag_c = [False] * 15

    def put() -> None:
        for i in range(8):
            print(f"{pos[i]:2}", end=" ")
        print()

    def set(i: int):
        for j in range(8):
            if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + 7]:
                pos[i] = j
                if i == 7:
                    put()
                else:
                    flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                    set(i + 1)
                    flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

    set(0)


if __name__ == "__main__":
    queen8()
