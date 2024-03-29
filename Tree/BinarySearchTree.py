from DSQueue import DSQueue


class BinarySearchTreeNode:

    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return self.__display()

    def height(self):
        """Returns the height of tree."""
        if not self:
            return 0
        left_height = 0
        if self.left:
            left_height = self.left.height()
        right_height = 0
        if self.right:
            right_height = self.right.height()
        return 1 + max(left_height, right_height)

    def add_node(self, data):
        """Add new node the BST."""
        if self.data == data:
            return

        node = BinarySearchTreeNode(data)
        node.parent = self
        if data < self.data:
            # add to left sub tree
            if self.left:
                self.left.add_node(data)
            else:
                self.left = node
        else:
            # add to right subtree
            if self.right:
                self.right.add_node(data)
            else:
                self.right = node

    def in_order_traversal(self):
        """In order traversal."""
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
        """Post order traversal."""
        elements = []
        # Left Right Root
        # visit left sub tree
        if self.left:
            elements.extend(self.left.post_order_traversal())
        # visit right sub tree
        if self.right:
            elements.extend(self.right.post_order_traversal())
        # visit base node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        """Pre order traversal."""
        # Root Left Right
        # visit base node
        elements = [self.data]
        # visit left sub tree
        if self.left:
            elements.extend(self.left.pre_order_traversal())
        # visit right sub tree
        if self.right:
            elements.extend(self.right.pre_order_traversal())

        return elements

    def level_order_traversal_or_bfs(self):
        if not self:
            return

        result = []
        q = DSQueue.Queue()
        q.enqueue(self)
        while not q.is_empty():
            node = q.dequeue()
            result.append(node.data.data)
            if node.data.left:
                q.enqueue(node.data.left)
            if node.data.right:
                q.enqueue(node.data.right)

        return result

    def search(self, value):
        """Search a value in BST."""
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

    def kth_largest(self, k):
        """Find the k-th largest item in BST."""
        if not k:
            return self.data, k
        data = None
        # Right Root Left
        if self.right and k:
            data, k = self.right.kth_largest(k)
        if k:
            data, k = self.data, k - 1
        if self.left and k:
            data, k = self.left.kth_largest(k)
        return data, k

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def max_path_sum(self):
        """Maximum possible sum from one node to another."""
        if not self:
            return 0

        if not self.left and not self.right:
            return self.data

        left_sum = 0
        if self.left:
            left_sum = self.left.max_path_sum()

        right_sum = 0
        if self.right:
            right_sum = self.right.max_path_sum()

        if self.left and self.right:
            return max(left_sum, right_sum) + self.data

        if not self.left:
            return right_sum + self.data

        return left_sum + self.data

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

    def is_valid_bst(self):
        """Check if tree is a valid BST or not."""
        if not self:
            return True

        if self.left:
            return self.left.data < self.data

        if self.right:
            return self.right.data > self.data

        left_valid = True
        right_valid = True
        if self.left:
            left_valid = self.left.is_valid_bst()
        if self.right:
            right_valid = self.right.is_valid_bst()
        if not left_valid or not right_valid:
            return False

    def reverse(self):
        """Reverse the BST."""
        if not self:
            return
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.reverse()
        if self.right:
            self.right.reverse()

    def diameter(self):
        """Returns diameter of tree.
        The diameter of a tree (sometimes called the width) is the number of
        nodes on the longest path between two end nodes.
        - The diameter of tree’s left subtree
        - The diameter of tree’s right subtree
        - The longest path between leaves that goes through the root of tree
        (this can be computed from the heights of the subtrees of tree)
        """
        if not self:
            return 0
        left_height = 0
        right_height = 0
        if self.left:
            left_height = self.left.height()
        if self.right:
            right_height = self.right.height()

        left_diameter = 0
        right_diameter = 0

        if self.left:
            left_diameter = self.left.diameter()
        if self.right:
            right_diameter = self.right.diameter()

        _diameter = max(left_diameter, right_diameter)
        return max(left_height + right_height + 1, _diameter)

    def __display(self, output='', node_pos='Root', level=0):
        """Display human readable BST."""
        if not self:
            return output
        parent = None
        if self.parent:
            parent = self.parent.data
        output += '{}{}-->{} [parent={}]\n'.format(
            '|  ' * level, node_pos, self.data, parent)
        if self.left:
            output = self.left.__display(
                output=output, node_pos='Left', level=level + 1)
        if self.right:
            output = self.right.__display(
                output=output, node_pos='Right', level=level + 1)
        return output

    def get_node_level(self, node):
        """Get the node level value in the BST."""
        level = 0
        while node != self:
            level += 1
            node = node.parent

        return level

    @staticmethod
    def backtrack_common_ancestor(descendant_one, descendant_two, depth_diff):
        """Back track to the common ancestor."""
        while depth_diff > 0:
            descendant_one = descendant_one.parent
            depth_diff -= 1

        while descendant_one is not descendant_two:
            descendant_one = descendant_one.parent
            descendant_two = descendant_two.parent

        return descendant_one

    def least_common_ancestor(self, descendant_one, descendant_two):
        """Find least common ancestor of two nodes."""
        descendant_one_level = self.get_node_level(descendant_one)
        descendant_two_level = self.get_node_level(descendant_two)

        if descendant_one_level > descendant_two_level:
            return self.backtrack_common_ancestor(
                descendant_one, descendant_two,
                descendant_one_level - descendant_two_level)
        else:
            return self.backtrack_common_ancestor(
                descendant_two, descendant_one,
                descendant_two_level - descendant_one_level)


def build_bst(elements):
    root = BinarySearchTreeNode(data=elements[0])
    for i in range(1, len(elements)):
        root.add_node(elements[i])

    return root


def build_tree_from_give_inorder(in_order, start=0, end=None):
    if not len(in_order):
        return None

    if end is None:
        end = len(in_order) - 1

    if start > end:
        return None

    size = len(in_order[start:end])
    middle = size // 2
    root = BinarySearchTreeNode(data=in_order[middle])

    root.left = build_tree_from_give_inorder(
        in_order[0: middle], start=0, end=middle)

    root.right = build_tree_from_give_inorder(
        in_order[middle + 1:], start=0, end=size)
    return root


def build_tree_from_give_preorder(
        pre_order, index=0, data=None, minimum=None, maximum=None):
    if not len(pre_order):
        return None, index

    if index >= len(pre_order):
        return None, index

    if data is None:
        data = pre_order[0]

    if minimum is None:
        minimum = -float('inf')

    if maximum is None:
        maximum = float('inf')

    root = None
    if minimum < data < maximum:
        root = BinarySearchTreeNode(data=data)
        index += 1

        if index < len(pre_order):
            root.left, index = build_tree_from_give_preorder(
                pre_order, index=index, data=pre_order[index],
                minimum=minimum, maximum=data)

            root.right, index = build_tree_from_give_preorder(
                pre_order, index=index, data=pre_order[index],
                minimum=data, maximum=maximum)

    return root, index


def build_tree_from_give_postorder(
        post_order, index=None, data=None, minimum=None, maximum=None):
    if not len(post_order):
        return None, index

    if index is None:
        index = len(post_order) - 1

    if index < 0:
        return None, index

    if data is None:
        data = post_order[index]

    if minimum is None:
        minimum = -float('inf')

    if maximum is None:
        maximum = float('inf')

    root = None
    if minimum < data < maximum:
        root = BinarySearchTreeNode(data=data)
        index -= 1

        if index >= 0:
            root.right, index = build_tree_from_give_postorder(
                post_order, index=index, data=post_order[index],
                minimum=data, maximum=maximum)

            root.left, index = build_tree_from_give_postorder(
                post_order, index=index, data=post_order[index],
                minimum=minimum, maximum=data)
    return root, index


if __name__ == '__main__':
    nums = [17, 4, 1, 9, 4, 20, 18, 34, 1, 23, 15, 50, 90, 55]
    num_tree = build_bst(nums)
    print('Min Max: ', num_tree.find_max(), num_tree.find_min())
    print('In Order: ', num_tree.in_order_traversal())
    print(num_tree)
    print('Pre Order: ', num_tree.pre_order_traversal())
    print('Post Order: ', num_tree.post_order_traversal())
    print('BFS: ', num_tree.level_order_traversal_or_bfs())
    num_tree.delete(20)
    print('2nd Largest: ', num_tree.kth_largest(2))
    print('Least Common Ancestor: \n', num_tree.least_common_ancestor(
        num_tree.left, num_tree.right.right))
    print('Height: ', num_tree.height())
    print('Diameter: ', num_tree.diameter())
    print('Is Valid BST: ', num_tree.is_valid_bst())
    print(num_tree)
    print('Max Sum Path: ', num_tree.max_path_sum())

    print('========================================')
    _inorder = [1, 4, 9, 15, 17, 18, 20, 23, 34, 50, 55, 90]
    dataTree = build_tree_from_give_inorder(_inorder)
    print(dataTree.in_order_traversal())
    print(dataTree)

    _pre_order = [10, 5, 1, 7, 40, 50]
    dataTree, _ = build_tree_from_give_preorder(_pre_order)
    print(dataTree.pre_order_traversal())
    print(dataTree)

    post = [1, 7, 5, 50, 40, 10]
    dataTree, _ = build_tree_from_give_postorder(post)
    print(dataTree.in_order_traversal())
    print(dataTree)
