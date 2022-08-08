class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            # add to left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # Left Root Right
        # visit left sub tree
        if self.left:
            elements.extend(self.left.in_order_traversal())
        # visit base node
        elements.append(self.data)
        # visit right sub tree
        if self.right:
            elements.extend(self.right.in_order_traversal())

        return elements

    def post_order_traversal(self):
        elements = []

        # Left Right Root
        # visit left sub tree
        if self.left:
            elements.extend(self.left.in_order_traversal())
        # visit right sub tree
        if self.right:
            elements.extend(self.right.in_order_traversal())
        # visit base node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        # Root Left Right
        # visit base node
        elements = [self.data]
        # visit left sub tree
        if self.left:
            elements.extend(self.left.in_order_traversal())
        # visit right sub tree
        if self.right:
            elements.extend(self.right.in_order_traversal())

        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            # value might be in right sub tree
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_min()

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    nums = [17, 4, 1, 9, 4, 20, 18, 34, 1, 23]
    num_tree = build_tree(nums)
    print('Min Max: ', num_tree.find_max(), num_tree.find_min())
    print('In Order: ', num_tree.in_order_traversal())
    print('Pre Order: ', num_tree.pre_order_traversal())
    print('Post Order: ', num_tree.post_order_traversal())
    num_tree.delete(20)
    print('Delete 20: ', num_tree.in_order_traversal())
    num_tree.delete(17)
    print('Delete 17: ', num_tree.in_order_traversal())
    num_tree.delete(9)
    print('Delete 9: ', num_tree.in_order_traversal())
    countries = [
        'India', 'Pakistan', 'UK', 'Germany',
        'USA', 'China', 'India', 'UK', 'USA',
    ]
    countries_tree = build_tree(countries)
    print(countries_tree.in_order_traversal())
    print(countries_tree.search('China'))
    print(countries_tree.search('india'))
