class MinHeap:

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

    def is_empty(self):
        return self.__size == 0

    def __swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def __min_heapify(self, pos):
        left = self.left_child(pos)
        right = self.right_child(pos)
        smallest = pos

        if self.__size >= left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if self.__size >= right and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != pos:
            self.__swap(pos, smallest)
            self.__min_heapify(smallest)

    def __float_up(self, pos):
        """Sets front/root node always smaller than inserted item."""
        parent = self.parent(pos)
        if parent < 1:
            return

        if self.heap[pos] < self.heap[parent]:
            self.__swap(pos, parent)
            self.__float_up(parent)

    def __display(self, output='', index=None, indent=''):
        """Str representation utility function."""
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

    def min_heapify(self):
        for pos in range(self.__size // 2, 0, -1):
            self.__min_heapify(pos)

    def insert(self, element):
        """Insert a new node."""
        self.__size += 1
        self.heap.append(element)
        self.__float_up(self.__size - 1)

    def pop(self):
        if not self.__size:
            return False

        if self.__size == 1:
            self.__size -= 1
            return self.heap.pop()

        self.__swap(self.__front, self.__size)
        popped = self.heap.pop()
        self.__size -= 1
        self.__min_heapify(self.__front)
        return popped

    def get_min(self):
        if self.__size:
            return self.heap[self.__front]

    def clear(self):
        self.heap = [0]
        self.__size = 0
        self.__front = 1


if __name__ == '__main__':
    minHeap = MinHeap()
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(1)
    minHeap.insert(28)
    minHeap.insert(12)
    minHeap.insert(2)
    minHeap.min_heapify()

    print(minHeap)
    print(minHeap.heap)
    print('Min val: {}'.format(minHeap.pop()))
