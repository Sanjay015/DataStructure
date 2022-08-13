def shell_sort(elements):
    # Optimization of insertion sort
    # 1. Start with gap = n/2 ans sort su=b arrays
    # 2. Keep reducing gap by n/2 in and keep on sorting subarrays
    # 3. Last iteration should be gap=1, now it is same as insertion sort
    # Time complexity O(n ^ 2)
    if len(elements) <= 0:
        return

    size = len(elements)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j >= gap and elements[j - gap] > anchor:
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = anchor
        gap = gap // 2


if __name__ == '__main__':
    test_cases = [
        [21, 28, 29, 17, 4, 25, 11, 32, 9],
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [],
        [7],
    ]
    for _elements in test_cases:
        shell_sort(_elements)
        print(_elements)
