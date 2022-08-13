class DEQueueFullException(Exception):
    pass


class Node:

    def __init__(self, data=None, _next=None):
        self.data = data
        self._nextNode = _next

    def __str__(self):
        return '{}'.format(self.data)

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, data):
        self._nextNode = data


class DEQueue:

    def __init__(self, max_size=100):
        self._front = None
        self._rear = None
        self._size = 0
        self._max_size = max_size

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

    def enqueue_front(self, data):
        if len(self) == self._max_size:
            raise DEQueueFullException('Queue full, cannon enqueue more items.')
        node = Node(data=data, _next=self._front)
        if self._front is None:
            self._rear = node
        self._front = node
        self._size += 1

    def enqueue_rear(self, data):
        if len(self) == self._max_size:
            raise DEQueueFullException('Queue full, cannon enqueue more items.')
        node = Node(data=data)
        if self._front is None:
            self._front = node

        if self._rear:
            self._rear.nextNode = node
        else:
            self._rear = node
        self._rear = node
        self._size += 1

    def dequeue_front(self):
        if self.is_empty():
            return
        node = self._front
        self._front = node.nextNode
        if self._front is None:
            self._rear = None

        self._size -= 1

    def dequeue_rear(self):
        if self.is_empty():
            return
        current_node = self._front
        prev_node = None
        while current_node.nextNode:
            prev_node = current_node
            current_node = current_node.nextNode

        if not prev_node:
            self._front = self._rear = None
            self._size -= 1
            return

        prev_node.nextNode = current_node.nextNode
        self._rear = prev_node
        self._size -= 1

    def peek(self):
        return self._front

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._max_size


if __name__ == '__main__':
    dequeue = DEQueue()
    dequeue.enqueue_front(10)
    dequeue.enqueue_front(20)
    dequeue.enqueue_front(15)
    dequeue.enqueue_rear(5)
    dequeue.enqueue_rear(9)
    dequeue.enqueue_rear(29)
    print(dequeue)
    dequeue.dequeue_front()
    dequeue.dequeue_rear()
    print(dequeue)
