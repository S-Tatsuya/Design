from typing import MutableSequence


def insertion_sort(datas: MutableSequence) -> MutableSequence:
    result = datas
    n = len(result)
    for i in range(1, n):
        j = i
        tmp = result[i]
        while j > 0 and result[j - 1] > tmp:
            result[j] = result[j - 1]
            j -= 1
        result[j] = tmp
    return result


def binary_insertion_sort(datas: MutableSequence) -> MutableSequence:
    result = datas
    n = len(result)
    for i in range(1, n):
        key = result[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2
            if result[pc] == key:
                break
            elif result[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            result[j] = result[j - 1]
        result[pd] = key
    return result
