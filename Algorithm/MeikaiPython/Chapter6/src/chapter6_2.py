def bubble_sort1(target: list[int]) -> list[int]:
    result = target
    for i in range(len(result) - 1):
        for j in reversed(range(i + 1, len(result))):
            if result[j] < result[j - 1]:
                result[j - 1], result[j] = result[j], result[j - 1]

    return result
