class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next_ = next_

    def __str__(self):
        return '{}'.format(self.data)


class Stack:
    def __init__(self):
        self.tos = None
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def push(self, data):
        self.tos = Node(data, self.tos)
        self.n += 1

    def pop(self):
        self.tos = self.tos.next_
        self.n -= 1

    def peek(self):
        return self.tos.data

    def __len__(self):
        return self.n

    def __str__(self):
        stack = ['tos']
        curr = self.tos
        while curr:
            stack.append('{}'.format(curr))
            curr = curr.next_
        return '---->'.join(stack[::-1])
