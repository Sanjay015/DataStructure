class Node:

    def __init__(self, data=None, next_=None):
        self.next = next_
        self.data = data


class Stack:

    def __init__(self, tos=None):
        self.tos = tos
        self.length = 0

    def push(self, data):
        node = Node(data=data, next_=self.tos)
        self.tos = node
        self.length += 1
        return node

    def pop(self):
        if not self.tos:
            return None
        node = self.tos
        self.tos = node.next
        self.length -= 1
        return node

    def peek(self):
        return self.tos

    def is_empty(self):
        return self.length == 0

    def __len__(self):
        return self.length


def pass_trucks(trucks):
    stack = Stack()
    possibility = True
    last_pass = None

    for i in range(len(trucks) - 1):
        if trucks[i] > trucks[i + 1]:
            if stack.tos and stack.tos.data < trucks[i]:
                possibility = False
                break
            stack.push(trucks[i])
        else:
            if last_pass and last_pass < trucks[i + 1]:
                possibility = False
                break
            last_pass = trucks[i]

    return possibility


if __name__ == '__main__':
    trucks_ = [5, 1, 3, 4, 2]
    print(pass_trucks(trucks_))
    # print(pass_trucks([4, 1, 5, 3, 2]))
    # print(pass_trucks([6, 5, 4, 3, 2, 1]))
    # json parser
    # expression resolution example (())) () [] {{{{}}}}
