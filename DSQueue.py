class QueueFullException(Exception):
    pass


class Node:

    def __init__(self, data=None, _next=None):
        self._nextNode = _next
        self.data = data

    def __str__(self):
        return '{}'.format(self.data)

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, node):
        self._nextNode = node


class Queue:

    def __init__(self, max_size):
        self._front = None
        self._rear = None
        self._size = 0
        self.maxSize = max_size

    def __len__(self):
        return self._size

    def __str__(self):
        output = ''
        curr = self._front
        while curr:
            if output:
                output = '{}->{}'.format(output, str(curr))
            else:
                output = '{}'.format(str(curr))
            curr = curr.nextNode
        return '[{}]'.format(output)

    def front(self):
        return self._front

    def rear(self):
        return self._rear

    def enqueue(self, data):
        if len(self) == self.maxSize:
            raise QueueFullException('Queue full, cannon enqueue more items.')
        self._size += 1
        node = Node(data=data)
        if self._rear is None:
            self._rear = self._front = node
            return

        self._rear.nextNode = node
        self._rear = node

    def dequeue(self):
        if self.is_empty():
            return

        node = self._front
        self._front = node.nextNode
        if self._front is None:
            self._rear = None

        self._size -= 1

    def is_empty(self):
        return self._front is None

    def is_full(self):
        return len(self) == self.maxSize

    def peek(self):
        return self._front.data

    def display(self):
        return str(self)


if __name__ == '__main__':
    q = Queue(100)
    q.enqueue('X')
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')
    print(q)
    print(len(q), q.is_full())
    print('Front: ', q.front(), 'Rear: ', q.rear())
    q.dequeue()
    print(q)
    print(len(q), q.is_full())
    print('Front: ', q.front(), 'Rear: ', q.rear())
    print(q.display())

