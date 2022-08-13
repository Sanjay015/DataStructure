def insertion_sort(elements):
    # Space complexity O(n)
    # Time complexity O(n ^ 2)
    if len(elements) <= 1:
        return

    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor


if __name__ == '__main__':
    test_cases = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [],
        [7],
    ]

    for _elements in test_cases:
        insertion_sort(_elements)
        print(_elements)

