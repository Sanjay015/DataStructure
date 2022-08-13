def _swap(first_index, second_index, array):
    if first_index != second_index:
        tmp = array[first_index]
        array[first_index] = array[second_index]
        array[second_index] = tmp


def _partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            _swap(start, end, elements)

    _swap(pivot_index, end, elements)
    return end


def quick_sort(elements, start=None, end=None):
    # Time complexity O(n ^ 2)
    # Create pivot and partition(left/right)
    # First element in partition is pivot initially
    # Start comparing pivot from start pointer until item > pivot, then stop the
    # start pointer and move to end pointer. Start decreasing end pointer until
    # item is < pivot. Stop when end < stop, then swap end with pivot.
    if len(elements) <= 0:
        return elements

    if start is None:
        start = 0

    if end is None:
        end = len(elements) - 1

    if start < end:
        partition_index = _partition(elements, start, end)
        # Left partition
        quick_sort(elements, start, partition_index - 1)
        # Right partition
        quick_sort(elements, partition_index + 1, end)


if __name__ == '__main__':
    test_cases = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [],
        [7],
        [30, 20],
    ]
    for _elements in test_cases:
        quick_sort(_elements)
        print(_elements)
