def _merger(first_array, second_array, array):
    i = j = k = 0
    while i < len(first_array) and j < len(second_array):
        if first_array[i] < second_array[j]:
            array[k] = first_array[i]
            i += 1
        else:
            array[k] = second_array[j]
            j += 1
        k += 1

    while i < len(first_array):
        array[k] = first_array[i]
        i += 1
        k += 1

    while j < len(second_array):
        array[k] = second_array[j]
        j += 1
        k += 1


def merge_sort(elements):
    # Space complexity O(n)
    # Time complexity O(n log(n))
    if len(elements) <= 1:
        return elements

    mid_index = len(elements) // 2

    left = elements[:mid_index]
    right = elements[mid_index:]

    merge_sort(left)
    merge_sort(right)

    _merger(left, right, elements)


if __name__ == '__main__':
    test_cases = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [],
        [7],
    ]
    for _elements in test_cases:
        merge_sort(_elements)
        print(_elements)
