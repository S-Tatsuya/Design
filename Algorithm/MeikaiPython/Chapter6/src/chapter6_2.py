from typing import MutableSequence


def bubble_sort1(target: list[int]) -> list[int]:
    result = target
    n = len(result)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in reversed(range(k + 1, len(result))):
            if result[j] < result[j - 1]:
                result[j - 1], result[j] = result[j], result[j - 1]
                last = j
        k = last

    return result


def bubble_sort_verbose(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(n - 1):
        print(f"パス{i + 1}")
        exchng = 0
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(
                    f"{a[m]:2}"
                    + ("  " if m != j - 1 else " +" if a[j - 1] > a[j] else " -"),
                    end="",
                )
            print(f"{a[n - 1]:2}")
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        for m in range(0, n - 1):
            print(f"{a[m]:2}", end="  ")
        print(f"{a[n - 1]:2}")
        if exchng == 0:
            break
    print(f"比較は{ccnt}回でした。")
    print(f"交換は{scnt}回でした。")


if __name__ == "__main__":
    bubble_sort_verbose([6, 4, 3, 7, 1, 9, 8])
    bubble_sort_verbose([1, 3, 9, 4, 7, 8, 6])
