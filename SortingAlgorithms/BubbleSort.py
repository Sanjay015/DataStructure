def bubble_sort(elements):
    # Space complexity O(n)
    # Time complexity O(n ^ 2)
    for i in range(len(elements) - 1):
        swapped = False
        for j in range(len(elements) - i - 1):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    _elements = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(_elements)
    print(_elements)


