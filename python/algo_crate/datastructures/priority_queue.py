from algo_crate.util import DEFAULT_CMP
from algo_crate.datastructures.heap import MinHeap


class PriorityQueue:

    def __init__(self, *values, key=lambda x: x):
        self.key = key
        self.q = MinHeap(*values, cmp=lambda x, y: DEFAULT_CMP(key(x), key(y)))

    def is_empty(self):
        return len(self) == 0

    def decrease_key(self, x):
        i = self.q.a.index(x)
        assert i != -1, f"Item {x} not in queue"

        k = self.key(x)
        self.q.decrease_key(i, k)

    def enqueue(self, x):
        self.q.insert(x)

    def dequeue(self):
        assert not self.is_empty(), "Queue underflow"
        return self.q.extract_min()

    def __contains__(self, x):
        return x in self.q

    def __len__(self):
        return len(self.q)

    def __str__(self):
        return f"PriorityQueue: front -> {self.q} <- tail"