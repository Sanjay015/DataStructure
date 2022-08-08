class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.val:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        root.height = 1 + max(
            self.get_height(root.left), self.get_height(root.right))
        # Get the balance factor
        balance = self.get_balance(root)
        # If the node is unbalanced, then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and value < root.left.val:
            return self.right_rotate(root)
        # Case 2 - Right Right
        if balance < -1 and value > root.right.val:
            return self.left_rotate(root)
        # Case 3 - Left Right
        if balance > 1 and value > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Case 4 - Right Left
        if balance < -1 and value < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def delete(self, root, value):
        if not root:
            return root 
        elif value < root.val:
            root.left = self.delete(root.left, value)
        elif value > root.val:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        if root is None:
            return root
        root.height = 1 + max(
            self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def left_rotate(self, z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = 1 + max(
            self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(
            self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        z.height = 1 + max(
            self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(
            self.get_height(y.left), self.get_height(y.right))
        return y

    @staticmethod
    def get_height(root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root:
            return
        self.pre_order(root.left)
        self.pre_order(root.right)

    def display(self, curr_ptr, indent, last):
        if curr_ptr is not None:
            if last:
                print('{}R----{}'.format(indent, curr_ptr.val))
                indent += '     '
            else:
                print('{}L----{}'.format(indent, curr_ptr.val))
                indent += '|    '
            self.display(curr_ptr.left, indent, False)
            self.display(curr_ptr.right, indent, True)


if __name__ == '__main__':
    avlTree = AVLTree()
    rootNode = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        rootNode = avlTree.insert(rootNode, num)
    avlTree.display(rootNode, '', True)
    key = 13
    rootNode = avlTree.delete(rootNode, key)
    print('After Deletion: ')
    avlTree.display(rootNode, '', True)
