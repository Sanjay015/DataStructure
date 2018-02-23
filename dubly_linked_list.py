class Node(object):
    def __init__(self, data=None, prev=None, _next=None):
        self.data = data
        self.prev = prev
        self.next = _next
 
 
class DoublyList(object):
    def __init__(self):
        self.n = 0
        self.tail = None
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        # Time complexity O(1)
        new_node = Node(data)
        new_node.next = self.head  
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

        self.n += 1

    def append(self, data):
        data_node = Node(data)
        if self.head is None:
            self.head = self.tail = data_node
        else:
            data_node.prev = self.tail
            data_node.next = None
            self.tail.next = data_node
            self.tail = data_node
        self.n += 1
 
    def pop(self):
        # Complexity O(1)
        tail_node = self.tail
        to_be_tail = self.tail.prev
        to_be_tail.next = None
        tail_node.prev = None
        self.tail = to_be_last
        self.n -= 1
        return tail_node

    def remove_by_index(self, index):
        raise NotImplementedError()

    def remove_by_value(self, node_value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
                self.n -= 1
            current_node = current_node.next
  
    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev 
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev

    def search(self, data):
        # Time complexity - O(n)
        index = 0
        curr_node = self.head
        while curr_node and curr_node.next != data:
            curr_node = curr_node.next
            index += 1
        if curr_node:
            print('Found {} at index - {}'.format(data, index))

    def __len__(self):
        # Complexity O(1)
        return self.n

    def __str__(self):
        dll = ['head']
        currnode = self.head
        while currnode:
            dll.append(currnode.data)
            currnode = currnode.next
        return '--->'.join(dll)

