def selection_sort(elements):
    # Time complexity O(n ^ 2)
    if len(elements) <= 0:
        return elements

    for i in range(len(elements) - 1):
        min_index = i
        for j in range(min_index + 1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j
        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]


if __name__ == '__main__':
    test_cases = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [],
        [7],
        [25, 17],
        [25, 17, 32],
    ]
    for _elements in test_cases:
        selection_sort(_elements)
        print(_elements)
