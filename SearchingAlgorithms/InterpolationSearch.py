def interpolation_search(array, lo, hi, item):
    if lo <= hi and array[lo] <= x <= array[hi]:
        # pos = mx + c
        # m = (hi - lo) // (arr[hi] - arr[lo])
        m = (hi - lo) // (arr[hi] - arr[lo])
        pos = lo + (m * (item - arr[lo]))
        if array[pos] == item:
            return pos

        if array[pos] < item:
            return interpolation_search(array, pos + 1, hi, item)

        if array[pos] > item:
            return interpolation_search(array, lo, pos - 1, item)


if __name__ == '__main__':
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    n = len(arr)
    x = 18
    index = interpolation_search(arr, 0, n - 1, x)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")
