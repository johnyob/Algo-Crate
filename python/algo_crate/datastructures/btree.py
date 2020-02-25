class BTreeNode:

    def __init__(self, leaf=False):
        self.keys = []
        self.c = []
        self.leaf = leaf

    def is_full(self, t):
        return len(self.keys) == 2 * t - 1


class BTree:

    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(leaf=True)

    def insert(self, k):
        r = self.root

        if r.is_full(self.t):
            s = BTreeNode()
            self.root = s

            # Former root is now the 0th child of the new root s
            s.c.insert(0, r)
            self._split_child(s, 0)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

    def _split_child(self, x, i):
        y = x.c[i]
        z = BTreeNode(leaf=y.leaf)

        t = self.t

        # slide all children of x to the right and insert z at i + 1
        x.c.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])

        # keys of z are t to 2t - 1 (not inclusive)
        # keys of y is  0 to t - 1  (not inclusive)
        z.keys = y.keys[t: 2 * t - 1]
        y.keys = y.keys[0 : t - 1]

        # children of z are t to 2t elements of y.c
        if not y.leaf:
            z.c = y.c[t: 2 * t]
            y.c = y.c[0 : t - 1]

    def _insert_nonfull(self, x, k):
        i = len(x.keys) - 1

        if x.leaf:
            # insert a key
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            # insert a child
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1

            if x.c[i].is_full(self.t):
                self._split_child(x, i)

                # Determine which child we should descend to
                if k > x.keys[i]:
                    i += 1

            self._insert_nonfull(x.c[i], k)





