class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next_ = next_

    def __str__(self):
        return '{}'.format(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        # Time complexity O(1)
        self.head = None(data, self.head)
        self.n += 1

    def append(self, data):
        # Complexity is always O(n)
        if self.head is None:
            self.prepend(data)
            return
        curr_node = self.head
        while curr_node.next_:
            curr_node = curr_node.next_
        curr_node.next_ = Node(data)
        self.n += 1

    def insert(self, data, index):
        # Time complexity O(n)
        counter = 1
        if index == 0:
            self.prepend(data)
            return
        if len(self) <= index:
            print("""Length of list is {} (index 0 - {}), but mentioned\
                     index is  {}. Impossible insert operation""".format(
                        len(self), len(self) - 1, index))
            return
        curr_node = self.head
        while counter < index:
            curr_node = curr_node.next_
            counter += 1
        temp_node = curr_node.next_
        curr_node.next_ = Node(data, temp_node)
        self.n += 1

    def pop(self):
        # Time complexity O(n)
        if self.is_empty():
            print('Empty list. Nothing to pop.')
            return
        elif self.n == 1:
            self.head = None
            self.n -= 1
            return

        curr_node = self.head
        prev_node = curr_node
        while curr_node.next_:
            prev_node = curr_node
            curr_node = curr_node.next_
        temp_node = prev_node.next_
        prev_node.next_ = None
        self.n -= 1
        return temp_node

    def search(self, data):
        # Time complexity - O(n)
        index = 0
        curr_node = self.head
        while curr_node and curr_node.next_ != data:
            curr_node = curr_node.next_
        if curr_node:
            print('Found {} at index - {}'.format(data, index))

    def remove_on_index(self, index=0):
        # Time complexity O(n)
        if self.is_empty:
            print('Empty list. Nothing to remove.')
            return
        elif len(self) <= index:
            print("""Length of list is {} (index 0 - {}), but mentioned\
                     index is  {}. Impossible insert operation""".format(
                        len(self), len(self) - 1, index))
            return

        if index == 0:
            self.head = self.head.next_
            self.n -= 1
            return
        counter = 0
        curr_node = self.head
        prev_node = curr_node
        while counter < index:
            prev_node = curr_node
            curr_node = curr_node.next_
            counter += 1
        prev_node.next_ = curr_node.next_
        self.n -= 1


    def remove_on_data(self, data):
        # Time complexity O(n)
        if self.is_empty:
            print('Empty List. Nothing to remove.')
            return

        curr_node = self.head
        prev_node = None
        while curr_node and curr_node.next_ != data:
            prev_node = curr_node
            curr_node = curr_node.next_
        if prev_node is None:
            self.head = curr_node.next_
            self.n += 1
        elif curr_node:
            prev_node.next_ = curr_node.next_
            self.n += 1
        elif:
            print('No node to removed. Data {} not found iin list.'.format(data))

    def reverse(self):
        # Time complexity - O(n)
        curr_node = self.head
        prev_node = None
        while curr_node:
            next_node = curr_node.next_
            curr_node.next_ = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def __len__(self):
        # Time complexity - O(1)
        return self.n

    def __str__(self):
        sll = ['head']
        curr = self.head
        while curr:
            sll.append('{}'.format(curr))
            curr = curr.next_
        return '--->'.join(sll)
        