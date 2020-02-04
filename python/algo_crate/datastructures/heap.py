from math import floor

from algo_crate.util import DEFAULT_CMP, is_series


class Heap:

    @staticmethod
    def parent(i):
        return floor((i + 1) / 2) - 1

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def __init__(self, *values, cmp=DEFAULT_CMP):
        """
        Heap constructor.
        Fills the heap using the build heap procedure

        :param values: (series)
        """

        self.cmp = cmp

        if len(values) == 0:
            self.a = []
            return

        x = values[0]
        if not is_series(x):
            self.a = self.build_heap([x])
            return

        assert is_series(x)
        assert len(x) > 0

        self.a = self.build_heap(x)

    def __len__(self):
        return len(self.a)

    def is_leaf(self, i):
        # Returns whether element at a[i] is a leaft.
        # Based on i > floor(n / 2) - 1 => a[i] is a leaf

        return i > floor(len(self) / 2) - 1

    def build_heap(self, values):

        heap = list(values)
        for i in range(Heap.parent(len(self)), -1, -1):
            self.heapify(heap, i)
        return heap

    def heapify(self, heap, i):

        raise NotImplementedError


class MaxHeap(Heap):

    def __init__(self, *values, cmp=DEFAULT_CMP):
        super().__init__(*values, cmp)

    def heapify(self, heap, i):

        l = Heap.left(i)
        r = Heap.right(i)

        largest = l if l < len(heap) and self.cmp(heap[l], heap[i]) > 0 else i
        largest = r if r < len(heap) and self.cmp(heap[r], heap[largest]) > 0 else largest

        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            self.heapify(heap, largest)

    def max(self):
        assert len(self) > 0

        return self.a[0]

    def extract_max(self):

        assert len(self) > 0

        self.a[0], self.a[-1] = self.a[-1], self.a[0]
        max = self.a.pop()
        self.heapify(self.a, 0)

        return max

    def insert(self, k):

        i = len(self)
        self.a.append(k)

        p = Heap.parent(i)
        while i > -1 and self.cmp(self.a[p], self.a[i]) < 0:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i, p = p, Heap.parent(p)


class MinHeap(Heap):

    def __init__(self, *values, cmp=DEFAULT_CMP):
        super().__init__(*values, cmp)

    def heapify(self, heap, i):

        l = Heap.left(i)
        r = Heap.right(i)

        smallest = l if l < len(heap) and self.cmp(heap[l], heap[i]) < 0 else i
        smallest = r if r < len(heap) and self.cmp(heap[r], heap[smallest]) < 0 else smallest

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(heap, smallest)

    def min(self):
        assert len(self) > 0

        return self.a[0]

    def extract_min(self):

        assert len(self) > 0

        self.a[0], self.a[-1] = self.a[-1], self.a[0]
        min = self.a.pop()
        self.heapify(self.a, 0)

        return min

    def insert(self, k):

        i = len(self)
        self.a.append(k)

        p = Heap.parent(i)
        while i > -1 and self.cmp(self.a[p], self.a[i]) > 0:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i, p = p, Heap.parent(p)

