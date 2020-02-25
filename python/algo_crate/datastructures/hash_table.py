from random import choice

from algo_crate.datastructures.linked_list import LinkedList


class HashFunction:
    # An implementation of universal hashing

    def __init__(self, p, m):
        # ASSERT: p is prime such that forall k. k < p.

        self.m = m
        self.p = p

        self.H = [self.h_ab(a, b) for a in range(1, p) for b in range(0, p)]

    def h_ab(self, a, b):
        return lambda k: ((a * k + b) % self.p) % self.m

    def __call__(self, x):
        assert x < self.p, f"Universal hashing doesn't allow for keys above {self.p}"
        return choice(self.H)(x)


class HashTable:

    def __init__(self, m):
        self.m = m

    def insert(self, x):
        raise NotImplementedError

    def delete(self, x):
        raise NotImplementedError

    def search(self, x):
        raise NotImplementedError


class ChainedHashTable(HashTable):

    def __init__(self, m=10):
        super().__init__(m)
        self.table = [LinkedList() for _ in  range(m)]
        self.h = HashFunction(p=347, m=m)

    def insert(self, x):
        self.table[self.h(x)].insert(x)

    def delete(self, x):
        self.table[self.h(x)].delete(x)

    def search(self, x):
        return self.table[self.h(x)].search(x)
