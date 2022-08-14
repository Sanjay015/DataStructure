def binary_search(array, item, start=None, end=None):
    # Time complexity O(log n)
    if start is None:
        start = 0

    if end is None:
        end = len(array) - 1

    if end >= start:
        mid = start + (end - start) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, item, start=start, end=mid - 1)
        else:
            return binary_search(array, item, start=mid + 1, end=end)


def exponential_search(array, item):
    if array[0] == item:
        return 0

    # Find range for binary search
    # j by repeated doubling
    i = 1
    while i < n and array[i] <= x:
        i = i * 2

    return binary_search(array, item, start=i // 2, end=min(i, len(array) - 1))


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 10
    result = exponential_search(arr, x)
    if result is None:
        print('Element not found in the array')
    else:
        print('Element is present at index: {}'.format(result))
