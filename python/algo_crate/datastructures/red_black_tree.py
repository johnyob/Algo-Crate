
from algo_crate.datastructures.binary_search_tree import Node

from enum import Enum


class Color(Enum):

    BLACK = 0
    RED = 1


class RedBlackNode(Node):

    def __init__(self, key, parent=None, left=None, right=None, color=Color.RED):
        super().__init__(key, parent, left, right)
        self.color = color

    def __repr__(self):
        if self.left is None and self.right is None:
            return "NIL"

        left = "\t".join(str(self.left).splitlines(True))
        right = "\t".join(str(self.right).splitlines(True))
        return f"Node: key: {self.key}, color: {self.color} \n" \
               f"left: {left} \n" \
               f"right: {right}"


class RedBlackTree:

    NIL = RedBlackNode(None, color=Color.BLACK)

    def __init__(self):
        self.root = self.NIL

    def is_empty(self):
        return self.root is self.NIL

    def left_rotate(self, x):
        assert x is not self.NIL

        y = x.right
        x.right = y.left

        if y.left is not self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is self.NIL:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        assert x is not self.NIL

        y = x.left
        x.left = y.right

        if y.right is not self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is self.NIL:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

    def _find_parent(self, k):
        x = self.root
        y = self.NIL

        while x is not self.NIL:
            # ASSERT: x is not a leaf and y is the pointer to x's parent
            y = x
            x = x.left if k < x.key else x.right

        return y

    def transplant(self, u, v):
        assert u is not self.NIL

        if u.parent is self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def insert_all(self, ks):
        for k in ks:
            self.insert(k)

    def insert(self, k):

        y = self._find_parent(k)
        z = RedBlackNode(k, y, self.NIL, self.NIL, color=Color.RED)

        if y is self.NIL:
            self.root = z
        elif k < y.key:
            y.left = z
        else:
            y.right = z

        self._insert_fixup(z)

    def _insert_fixup(self, z):
        """
        Given a red child node, determine whether we need to fixup (that is if the parent is red)

        :param z:
        :return:
        """

        while z.parent.color == Color.RED:
            # ASSERT   I: z is red
            # ASSERT  II: z.parent is root => z.parent is black
            # ASSERT III: If the tree violates any of the properties, then it violates at most one property of either 2, 4.
            #             That is if z is the root, then z is red => violates property 2 (root is black)
            #             That is if z and z.parent are red => violates a red node having only black children

            # IMPLICATION: z.parent.parent (grandfather) exists since if z.parent is the root, then it follows that
            #              z.parent is black, hence the loop terminates. So z.parent.parent must exist.

            parent = z.parent
            grandfather = parent.parent

            if parent is grandfather.left:
                # ASSERT: z's parent is the left child of z's grandfather

                uncle = grandfather.right # z's uncle

                if uncle.color == Color.RED:
                    # ASSERT: z's uncle is red. This is case 1.
                    # IMPLICATION: Given the assumption that the RB tree is valid prior to insertion, then we have
                    # grandfather.color == Color.BLACK, since parent and uncle are red.

                    # Fix: recolor parent and uncle to black and grandfather to red.
                    # Potential violation: grandfather might violate property 2 or 4
                    #                      (depending on whether the grandfather is the root of the tree)

                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    grandfather.color = Color.RED

                    # Fix the potential violation
                    z = grandfather

                elif z is parent.right:
                    # ASSERT: z's uncle is black and z is the right child of z's parent. This is case 2 (the triangle case)

                    # Fix: rotate left (the opposite direction to z) on z's parent
                    # Potential violation: No introduction of new violation

                    z = parent
                    self.left_rotate(parent)
                else:
                    # ASSERT: z's uncle is black and z is the left child of z's parent. This is case 3 (the line case)

                    # IMPLICATION: Given the assumption that the RB tree is valid prior to insertion,
                    # then we grandfather.color == Color.BLACK, since parent is red.

                    # Fix: rotate right (the opposite direction to z) on z's grandfather and recolor
                    # Potential violation: No introduction of new violation

                    parent.color = Color.BLACK # The while loop now will terminate since parent is black.
                    grandfather.color = Color.RED

                    self.right_rotate(grandfather)
            else:
                # ASSERT: z's parent is the right child of z's grandfather

                uncle = grandfather.left # z's uncle

                if uncle.color == Color.RED:
                    # ASSERT: z's uncle is red. This is case 1.
                    # IMPLICATION: Given the assumption that the RB tree is valid prior to insertion, then we have
                    # grandfather.color == Color.BLACK, since parent and uncle are red.

                    # Fix: recolor parent and uncle to black and grandfather to red.
                    # Potential violation: grandfather might violate property 2 or 4
                    #                      (depending on whether the grandfather is the root of the tree)

                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    grandfather.color = Color.RED

                    # Fix the potential violation
                    z = grandfather

                elif z is parent.left:
                    # ASSERT: z's uncle is black and z is the left child of z's parent. This is case 2 (the triangle case)

                    # Fix: rotate right (the opposite direction to z) on z's parent
                    # Potential violation: No introduction of new violation (although doesn't fix previous violation)

                    z = parent
                    self.right_rotate(parent)
                else:
                    # ASSERT: z's uncle is black and z is the right child of z's parent. This is case 3 (the line case)

                    # IMPLICATION: Given the assumption that the RB tree is valid prior to insertion,
                    # then we grandfather.color == Color.BLACK, since parent is red.

                    # Fix: rotate left (the opposite direction to z) on z's grandfather and recolor
                    # Potential violation: No introduction of new violation

                    parent.color = Color.BLACK # The while loop now will terminate since parent is black.
                    grandfather.color = Color.RED

                    self.left_rotate(grandfather)

        # ASSERT: Property 2 holds
        self.root.color = Color.BLACK

    def delete_all(self, ks):
        for k in ks:
            self.delete(k)

    def delete(self, k):
        """

        :param k:
        :return:
        """

        z = self.search(k)
        assert z is not self.NIL

        y = z # DEFINE: y as the node either to be removed or to be moved
        y_color = y.color

        if z.left is self.NIL:
            # ASSERT: z.left is NIL

            x = z.right # DEFINE: x as the node that moves into y's position
            self.transplant(z, x)

        elif z.right is self.NIL:
            # ASSERT: z.left is not NIL

            x = z.left
            self.transplant(z, x)
        else:
            # ASSERT: z has 2 children
            y = self.min(z.right)
            y_color = y.color

            x = y.right
            if y.parent is z:
                x.parent = y

            self.delete(y.key)

            # Move y to z by changing z to y's key
            z.key = y.key

        # if y's original color is black, then we might've introduced a violation
        if y_color == Color.BLACK:
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        """
        Given the moved node, determine whether we need to fixup (that is if the moved node is doubly black)

        :param x:
        :return:
        """

        while x is not self.root and x.color == Color.BLACK:
            # ASSERT I: x is doubly black

            # IMPLICATION I: sibling of x cannot be NIL because would be bh(x.parent -> sibling) = bh(x.parent -> x)
            #                false

            parent = x.parent

            if x is parent.left:
                sibling = parent.right
                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.left_rotate(x.parent)
                    sibling = x.parent.right

                if sibling.left.color == Color.BLACK and sibling.right.color == Color.BLACK:
                    sibling.color = Color.RED
                    x = x.parent
                else:
                    if sibling.right.color == Color.BLACK:
                        sibling.left.color = Color.BLACK
                        sibling.color = Color.RED
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = Color.BLACK
                    sibling.right.color = Color.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = parent.left
                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.right_rotate(x.parent)
                    sibling = x.parent.left

                if sibling.right.color == Color.BLACK and sibling.left.color == Color.BLACK:
                    sibling.color = Color.RED
                    x = x.parent
                else:
                    if sibling.left.color == Color.BLACK:
                        sibling.right.color = Color.BLACK
                        sibling.color = Color.RED
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = Color.BLACK
                    sibling.left.color = Color.BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = Color.BLACK

    def search(self, k):
        x = self.root
        while x is not self.NIL and k != x.key:
            x = x.left if k < x.key else x.right

        return x

    def min(self, x=None):
        if x is None:
            x = self.root

        assert x is self.NIL, "Cannot find the minimum of an empty subtree"
        while x is not self.NIL:
            x = x.left

        return x

    def max(self, x=None):
        if x is None:
            x = self.root

        assert x is not self.NIL, "Cannot find the maximum of an empty subtree"
        while x is not self.NIL:
            x = x.right

        return x


