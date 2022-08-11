class MaxHeap:

    def __init__(self):
        self.size = 0
        self.heap = [0]
        self.front = 1

    def __str__(self):
        return self.display()

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
        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def max_heapify(self, pos):
        if self.is_leaf(pos):
            return

        if (self.heap[pos] > self.heap[self.left_child(pos)] and
                self.heap[pos] > self.heap[self.right_child(pos)]):
            return

        # Swap with the left child and heapify
        # the left child
        if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)]:
            self.swap(pos, self.left_child(pos))
            self.max_heapify(self.left_child(pos))

        # Swap with the right child and heapify
        # the right child
        else:
            self.swap(pos, self.right_child(pos))
            self.max_heapify(self.right_child(pos))

    def insert(self, element):
        self.size += 1
        self.heap.append(element)

        current = self.size
        while (current > 1 and
               self.heap[current] > self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def display(self, output='', index=None, indent=None):
        # Function to print the contents of the heap
        if not self.size:
            return
        if index is None:
            index = 1
        if indent is None:
            indent = ''

        if index <= (self.size // 2):
            root = self.heap[index]
            left = self.heap[self.left_child(index)]
            if index == 1:
                output += 'Root--{}\n'.format(root)
            indent += '|  '
            output += '{}Left--{}\n'.format(indent, left)
            output = self.display(
                output=output, index=self.left_child(index), indent=indent)
            if self.size >= self.right_child(index):
                right = self.heap[self.right_child(index)]
                output += '{}Right--{}\n'.format(indent, right)
                output = self.display(
                    output=output, index=self.right_child(index), indent=indent)
        return output

    def extract_max(self):
        # Function to remove and return the maximum
        # element from the heap
        popped = self.heap[self.front]
        self.swap(self.front, self.size)
        self.heap.pop()
        self.size -= 1
        self.max_heapify(self.front)

        return popped


if __name__ == '__main__':
    # Driver Code
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
    print(maxHeap.heap, maxHeap.size)
    print('The Max val is ' + str(maxHeap.extract_max()))
    print(maxHeap.heap, maxHeap.size)
    print(maxHeap)
