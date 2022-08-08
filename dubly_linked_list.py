class Node:

    def __init__(self, data=None, _next=None, _prev=None):
        self._nextNode = _next
        self._prevNode = _prev
        self.data = data

    def __str__(self):
        return '{}'.format(self.data)

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, node):
        self._nextNode = node

    @property
    def prevNode(self):
        return self._prevNode

    @prevNode.setter
    def prevNode(self, node):
        self._prevNode = node


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        output = ''
        curr = self.head
        while curr:
            if output:
                output = '{}, {}'.format(output, str(curr))
            else:
                output = '{}'.format(str(curr))
            curr = curr.nextNode
        return '[{}]'.format(output)

    def __getitem__(self, index):
        return self.getByIndex(index)

    def __setitem__(self, index, data):
        if index >= len(self) or self.isEmpty():
            raise IndexError(
                ('length of list is: {}, you are trying to set value '
                 'at index: {}').format(len(self), index))
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.nextNode
            counter += 1
        current_node.data = data

    def __delitem__(self, index):
        return self.deleteByIndex(index)

    def __contains__(self, item):
        return self.search(item)

    def isEmpty(self):
        return self.head is None

    def prepend(self, data):
        node = Node(data=data, _next=self.head)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prevNode = node
            self.head = node
        self._size += 1

    def append(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prevNode = self.tail
            node.nextNode = None
            self.tail.nextNode = node
            self.tail = node
        self._size += 1

    def insert(self, index, data):
        if index >= len(self):
            raise IndexError(
                ('length of list is: {}, you are trying to insert value '
                 'at index: {}').format(len(self), index))

        if index == 0:
            return self.prepend(data)
        counter = 0
        current_node = self.head
        prev_node = current_node
        while counter != index:
            prev_node = current_node
            current_node = current_node.nextNode
            counter += 1

        node = Node(data=data, _next=current_node, _prev=prev_node)
        prev_node.nextNode = node
        current_node.prevNode = node
        self._size += 1

    def pop(self):
        if self.isEmpty():
            return

        tail = self.tail
        prev = tail.prevNode
        prev.nextNode = None
        tail.prevNode = None
        self.tail = prev
        self._size -= 1
        return tail

    def search(self, item):
        if self.isEmpty():
            return False
        current_node = self.head
        while current_node:
            if current_node.data == item:
                return True
            current_node = current_node.nextNode
        return False

    def getByIndex(self, index):
        if self.isEmpty():
            return

        if index >= len(self):
            raise IndexError(
                ('length of list is: {}, but you are trying to get value '
                 'at index: {}').format(len(self), index))

        counter = 0
        node = self.head
        while counter != index:
            node = node.nextNode
            counter += 1
        return node

    def deleteByIndex(self, index):
        if self.isEmpty() or index >= len(self):
            raise IndexError(
                ('length of list is: {}, you are trying to delete value '
                 'at index: {}').format(len(self), index))
        counter = 1
        current_node = self.head
        prev_node = current_node
        while counter < index:
            prev_node = current_node
            current_node = current_node.nextNode
            counter += 1
        tmp_node = current_node
        prev_node.nextNode = current_node.nextNode
        current_node.nextNode = None
        current_node.prevNode = None
        self._size -= 1
        return tmp_node

    def reverse(self):
        current_node = self.head
        self.tail = current_node
        prev_node = None

        while current_node:
            prev_node = current_node.prevNode
            current_node.prevNode = current_node.nextNode
            current_node.nextNode = prev_node
            current_node = current_node.prevNode

        if prev_node is not None:
            self.head = prev_node.prevNode


if __name__ == '__main__':
    doubly_list = DoublyLinkedList()
    doubly_list.prepend(10)
    doubly_list.prepend(20)
    doubly_list.append(5)
    doubly_list.append(6)
    # del doubly_list[3]
    doubly_list.insert(2, 80)
    # doubly_list.insert(2, 8)
    # doubly_list.insert(2, 88)
    # doubly_list[2] = 77
    print(len(doubly_list), doubly_list)
    doubly_list.reverse()
    print('reverse: ', doubly_list)
