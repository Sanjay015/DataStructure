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


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, items):
        return self.getByIndex(items)

    def __setitem__(self, index, data):
        return self.insert(index, data)

    def __delitem__(self, index):
        return self.deleteByIndex(index)

    def __contains__(self, item):
        return self.search(item)

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

    def isEmpty(self):
        return self.head is None

    def prepend(self, data):
        self.head = Node(data=data, _next=self.head)
        self._size += 1

    def append(self, data):
        if self.head is None:
            self.prepend(data)
            return
        node = Node(data=data)
        current_node = self.head
        while current_node.nextNode:
            current_node = current_node.nextNode
        current_node.nextNode = node
        self._size += 1

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return

        if len(self) <= index:
            raise IndexError(
                ('length of list is: {}, but you are trying to insert value '
                 'at index: {}').format(len(self), index))

        counter = 1
        current_node = self.head
        while counter < index:
            current_node = current_node.nextNode
            counter += 1
        node = Node(data=data, _next=current_node.nextNode)
        current_node.nextNode = node
        self._size += 1

    def pop(self):
        if self.isEmpty():
            return
        if len(self) == 1:
            self.head = None
            self._size -= 1
            return

        current_node = self.head
        prev_node = current_node
        while current_node.nextNode:
            prev_node = current_node
            current_node = current_node.nextNode
        tmp_node = prev_node.nextNode
        prev_node.nextNode = None
        self._size -= 1
        return tmp_node

    def getByIndex(self, index):
        if self.isEmpty():
            return
        if index >= len(self):
            raise IndexError(
                ('length of list is: {}, but you are trying to get value '
                 'at index: {}').format(len(self), index))
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.nextNode
            counter += 1
        return current_node

    def deleteByIndex(self, index):
        if self.isEmpty():
            return
        if index >= len(self):
            raise IndexError(
                ('length of list is: {}, but you are trying to get value '
                 'at index: {}').format(len(self), index))

        if index == 0:
            self.head = self.head.nextNode
            self._size -= 1
            return

        counter = 0
        current_node = self.head
        prev_node = current_node
        while counter != index:
            prev_node = current_node
            current_node = current_node.nextNode
            counter += 1
        node_to_delete = current_node
        prev_node.nextNode = current_node.nextNode
        self._size -= 1
        return node_to_delete

    def search(self, item):
        current_node = self.head
        while current_node:
            if current_node.data == item:
                return True
            current_node = current_node.nextNode
        return False

    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.nextNode
            current_node.nextNode = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(5)
    linked_list.prepend(2)
    print(linked_list)
    print('Get item--: ', linked_list[4])
    print('----search-', 50 in linked_list)
    linked_list.reverse()
    print('----reverse-', linked_list)
