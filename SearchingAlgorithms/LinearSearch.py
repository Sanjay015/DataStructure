def linear_search(array, item):
    length = len(array)
    right = length - 1

    for left in range(0, right, 1):
        if array[left] == item:
            return left

        if arr[right] == item:
            return right
        left += 1
        right -= 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    search_element = 5

    index = linear_search(arr, search_element)
    if index is None:
        print('Element not found in array')
    else:
        print('Element found at index: {}'.format(index))
