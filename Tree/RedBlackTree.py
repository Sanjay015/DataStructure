class Node:

    def __init__(self, data=None, right=None, left=None, color=0, parent=None):
        self.data = data
        self.left = right
        self.right = left
        self.parent = parent
        self.color = color  # 1 (RED), 0 (BLACK)
        self._color_map = {1: 'RED', 0: 'BLACK'}

    def __str__(self):
        left = right = parent = None
        if self.left is not None:
            left = self.left.data
        if self.right is not None:
            right = self.right.data
        if self.parent is not None:
            parent = self.parent.data
        return 'Node(data={}, color={}, left={}, right={}, parent={})'.format(
            self.data, self.color_map[self.color], left, right, parent)

    @property
    def color_map(self):
        return self._color_map


class RedBlackTree:

    def __init__(self):
        self.__NullNode = Node()
        self.root = self.__NullNode

    def __str__(self):
        return self.__display()

    def _is_leaf_node(self, node):
        if node == self.__NullNode:
            return True

        if node is None:
            return True

        if node.left is None and node.right is None:
            return True

        return False

    def insert(self, data):
        """Add new node the BST."""
        node = Node(
            data=data, left=self.__NullNode, right=self.__NullNode, color=1)
        parent_node = None
        current_node = self.root

        while current_node != self.__NullNode:
            parent_node = current_node
            if data < current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right
            else:
                return

        node.parent = parent_node

        if parent_node is None:
            self.root = node
        elif data < parent_node.data:
            parent_node.left = node
        else:
            parent_node.right = node

        # print(data, node.left, node.right)
        self.__insert_fix(node)

    def __insert_fix(self, node):
        while node != self.root and node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left  # uncle
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right  # uncle

                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
        self.root.color = 0

    def __delete_fix(self, node):
        while node != self.root and node.color == 0:
            if node == node.parent.left:
                _child = node.parent.right
                if _child.color == 1:
                    _child.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    _child = node.parent.right

                if _child.left.color == 0 and _child.right.color == 0:
                    _child.color = 1
                    node = node.parent
                else:
                    if _child.right.color == 0:
                        _child.left.color = 0
                        _child.color = 1
                        self.right_rotate(_child)
                        _child = node.parent.right

                    _child.color = node.parent.color
                    node.parent.color = 0
                    _child.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                _child = node.parent.left
                if _child.color == 1:
                    _child.color = 0
                    node.parent.color = 1
                    self.right_rotate(node.parent)
                    _child = node.parent.left

                if _child.right.color == 0 and _child.right.color == 0:
                    _child.color = 1
                    node = node.parent
                else:
                    if _child.left.color == 0:
                        _child.right.color = 0
                        _child.color = 1
                        self.left_rotate(_child)
                        _child = node.parent.left

                    _child.color = node.parent.color
                    node.parent.color = 0
                    _child.left.color = 0
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 0

    def __rb_transplant(self, to_delete, replace_with_node):
        if to_delete.parent is None:
            self.root = replace_with_node
        elif to_delete == to_delete.parent.left:
            to_delete.parent.left = replace_with_node
        else:
            to_delete.parent.right = replace_with_node
        replace_with_node.parent = to_delete.parent

    def delete(self, value, node=None):
        to_delete = self.__NullNode
        if node is None:
            node = self.root

        while node != self.__NullNode:
            if node.data == value:
                to_delete = node
                break
            if node.data < value:
                node = node.right
            else:
                node = node.left

        if to_delete == self.__NullNode:
            raise ValueError('Cannot find key: {} in the tree'.format(value))

        y = to_delete
        y_original_color = y.color
        if to_delete.left == self.__NullNode:
            _child = to_delete.right
            self.__rb_transplant(to_delete, to_delete.right)
        elif to_delete.right == self.__NullNode:
            _child = to_delete.left
            self.__rb_transplant(to_delete, to_delete.left)
        else:
            y = self.minimum(to_delete.right)
            y_original_color = y.color
            _child = y.right
            if y.parent == to_delete:
                _child.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = to_delete.right
                y.right.parent = y

            self.__rb_transplant(to_delete, y)
            y.left = to_delete.left
            y.left.parent = y
            y.color = to_delete.color

        if y_original_color == 0:
            self.__delete_fix(_child)

    def left_rotate(self, node):
        """Left rotation of Red Black Tree."""
        if self._is_leaf_node(node):
            return
        y = node.right

        if y == self.__NullNode:
            return

        node.right = y.left
        if y.left != self.__NullNode:
            y.left.parent = node

        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        """Right rotation of Red Black Tree."""
        if self._is_leaf_node(node):
            return
        y = node.left

        if y == self.__NullNode:
            return

        node.left = y.right
        if y.right != self.__NullNode:
            y.right.parent = node

        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def minimum(self, node):
        while node.left != self.__NullNode:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.__NullNode:
            node = node.right
        return node

    def search(self, value, node=None):
        if node == self.__NullNode or value == node.data:
            return node

        if value < node.data:
            return self.search(value, node=node.left)
        return self.search(value, node=node.right)

    def __display(self, node=None, output='', node_pos='Root', level=0):
        """Display human readable BST."""
        if node is None:
            node = self.root

        if node == self.__NullNode:
            return output
        parent = None
        color = node.color_map[node.color]
        if node.parent:
            parent = node.parent.data
        output += '{}{}-->{} (color={}) [parent={}]\n'.format(
            '|  ' * level, node_pos, node.data, color, parent)
        if node.left:
            output = self.__display(
                node=node.left, output=output, node_pos='Left', level=level + 1)
        if node.right:
            output = self.__display(
                node=node.right, output=output,
                node_pos='Right', level=level + 1)
        return output


if __name__ == '__main__':
    t = RedBlackTree()
    # t.insert(5)
    # t.insert(10)
    # t.insert(2)
    # t.insert(8)
    # t.insert(12)
    # t.insert(6)
    # t.insert(9)

    t.insert(10)
    t.insert(8)
    # t.insert(7)
    # t.insert(5)
    # t.insert(4)
    print(t)
    # print(t.root)
    # print(t.root.left)
    # print(t.root.right)
    print('==================================')
    t.left_rotate(t.root)
    print(t)
    t.delete(10)
    print(t)
    # print('==================================')
    # t.right_rotation(t.root)
    # print(t)
