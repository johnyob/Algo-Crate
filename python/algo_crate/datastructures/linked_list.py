class Node:

    def __init__(self, k, next=None, prev=None):
        self.k = k
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"Node: (prev: {self.prev}, k: {self.k}, next: {self.next})"


class LinkedList:

    def __init__(self):

        # Construct circular sentinel object
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

        self.len = 0

    def insert(self, k):
        x = Node(k, self.nil.next)

        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

        self.len += 1

    def search(self, k):
        x = self.nil.next
        while x != self.nil and x.k != k:
            x = x.next
        return x

    def delete(self, k):
        assert len(self) > 0, "List underflow"
        x = self.search(k)

        assert x is not None, f"Node with key {k} not in list L"

        x.prev.next = x.next
        x.next.prev = x.prev

    def __len__(self):
        return self.len

    def __repr__(self):
        return f"List: {list(iter(self))}."

    def __iter__(self):
        xs = []
        x = self.nil.next
        while x is not self.nil:
            xs.append(x.k)
            x = x.next
        return iter(xs)


