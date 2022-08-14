import math


def jump_search(array, item):
    # Time complexity O(n ^ 1/2)
    prev = 0
    size = len(array)
    jump_step = math.sqrt(size)

    while array[int(min(jump_step, size) - 1)] < item:
        prev = jump_step
        jump_step += math.sqrt(size)
        if prev >= size:
            return -1

    while array[prev] < item:
        prev += 1
        if prev == min(jump_step, size):
            return -1

    if array[int(prev)] == item:
        return prev


if __name__ == '__main__':
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    x = 55
    index = jump_search(arr, x, 4)
    if index is None:
        print('Element: {}, not found in array'.format(x))
    else:
        print('Number: {}, is at index:{} '.format(x, index))
