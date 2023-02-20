from typing import MutableSequence


def merge(a: MutableSequence, b: MutableSequence, c: MutableSequence):
    pa, pb, pc = 0, 0, 0
    na, nb = len(a), len(b)

    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1


def merge_sort(a: MutableSequence) -> MutableSequence:
    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    result = a
    n = len(result)
    buff = [None] * n
    _merge_sort(result, 0, n - 1)
    del buff
    return result
