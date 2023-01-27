from typing import MutableSequence


def selection_sort(datas: MutableSequence) -> MutableSequence:
    result = datas
    n = len(result)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if result[j] < result[min]:
                min = j
            result[i], result[min] = result[min], result[i]

    return result
