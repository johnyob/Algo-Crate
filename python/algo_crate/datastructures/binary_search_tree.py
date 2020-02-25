class Node:

    def __init__(self, key, parent=None, left=None, right=None):
        self.parent = parent
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def _find_parent(self, k):
        x = self.root
        y = None

        while x is not None:
            # ASSERT: x is not a leaf and y is the pointer to x's parent
            y = x
            if k < x.key:
                x = x.left
            else:
                x = x.right

        return y

    def transplant(self, u, v):
        assert u is not None

        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def insert_all(self, ks):
        for k in ks:
            self.insert(k)

    def insert(self, k):
        y = self._find_parent(k)

        # Create the new node z
        z = Node(k, y)

        # Insert the node
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def delete_all(self, ks):
        for k in ks:
            self.delete(k)

    def delete(self, k):
        x = self.search(k)

        if x is not None:
            if x.left is None and x.right is None:
                self.transplant(x, None)
            elif x.left is None:
                self.transplant(x, x.right)
            elif x.right is None:
                self.transplant(x, x.left)
            else:
                y = self.min(x.right)
                self.delete(y.key)
                x.key = y.key

    def search(self, k):
        x = self.root
        while x is not None and k != x.key:
            x = x.left if k < x.key else x.right

        return x

    def min(self, x=None):
        if x is None:
            x = self.root

        assert x is not None, "Cannot find the minimum of an empty subtree"
        while x is not None:
            x = x.left

        return x

    def max(self, x=None):
        if x is None:
            x = self.root

        assert x is not None, "Cannot find the maximum of an empty subtree"
        while x is not None:
            x = x.right

        return x

    def successor(self, x=None):
        if x is None:
            x = self.root

        assert x is not None, "Cannot find the successor of an empty subtree"
        if x.right is not None:
            return self.min(x.right)

        y = x.parent
        while y is not None and x == y.right:
            x, y = y, y.parent
        return y

    def predecessor(self, x=None):
        if x is None:
            x = self.root

        assert x is not None, "Cannot find the predecessor of an empty subtree"
        if x.left is not None:
            return self.max(x.left)

        y = x.parent
        while y is not None and x == y.left:
            x, y = y, y.parent
        return y

    def traverse(self, traversal_function):
        return traversal_function(self.root)
