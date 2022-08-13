class MaxHeap:

    def __init__(self):
        self.__size = 0
        self.heap = [0]
        self.__front = 1

    def __str__(self):
        return self.__display()

    def __len__(self):
        return self.__size

    @staticmethod
    def parent(pos):
        return pos // 2

    @staticmethod
    def left_child(pos):
        return 2 * pos

    @staticmethod
    def right_child(pos):
        return (2 * pos) + 1

    def is_leaf(self, pos):
        if (self.__size // 2) <= pos <= self.__size:
            return True
        return False

    def __swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def __max_heapify(self, pos):
        left = self.left_child(pos)
        right = self.right_child(pos)
        largest = pos

        if self.__size >= left and self.heap[largest] < self.heap[left]:
            largest = left
        if self.__size >= right and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != pos:
            self.__swap(pos, largest)
            self.__max_heapify(largest)

    def __float_up(self, pos):
        """Sets front/root node always larger than inserted item."""
        parent = self.parent(pos)
        if parent < 1:
            return

        if self.heap[pos] > self.heap[parent]:
            self.__swap(pos, parent)
            self.__float_up(parent)

    def __display(self, output='', index=None, indent=''):
        if not self.__size:
            return output

        if index is None:
            index = self.__front

        if index <= (self.__size // 2) + 1:
            if index == 1:
                output += 'Root--{}\n'.format(self.heap[self.__front])

            indent += '|  '

            if self.__size >= self.left_child(index):
                left = self.heap[self.left_child(index)]
                output += '{}Left--{}\n'.format(indent, left)
                output = self.__display(
                    output=output, index=self.left_child(index), indent=indent)

            if self.__size >= self.right_child(index):
                right = self.heap[self.right_child(index)]
                output += '{}Right--{}\n'.format(indent, right)
                output = self.__display(
                    output=output, index=self.right_child(index), indent=indent)

        return output

    def insert(self, element):
        self.heap.append(element)
        self.__size += 1
        self.__float_up(self.__size)

    def max_heapify(self):
        for pos in range(self.__size // 2, 0, -1):
            self.__max_heapify(pos)

    def peek(self):
        if self.__size:
            return self.heap[self.__front]

    def pop(self):
        if not self.__size:
            return False

        if self.__size == 1:
            self.__size -= 1
            return self.heap.pop()

        self.__swap(self.__front, self.__size)
        popped = self.heap.pop()
        self.__size -= 1
        self.__max_heapify(self.__front)
        return popped

    def get_max(self):
        if self.__size:
            return self.heap[self.__front]


if __name__ == '__main__':
    maxHeap = MaxHeap()
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)
    maxHeap.insert(99)
    maxHeap.max_heapify()
    print(maxHeap)
    print(maxHeap.heap)
    print('Max val: {}'.format(maxHeap.pop()))
