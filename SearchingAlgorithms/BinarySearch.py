def binary_search(array, item, start=None, end=None):
    # Time complexity O)log n)
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


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binary_search(arr, x)

    if result is None:
        print('Element is not present in array')
    else:
        print('Element is present at index: {}'.format(result))
