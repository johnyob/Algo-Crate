from algo_crate.util import DEFAULT_CMP
from algo_crate.datastructures.heap import MaxHeap

class PriorityQueue:

    def __init__(self, *values):
        self.q = MaxHeap(*values, cmp=lambda x, y: DEFAULT_CMP(x[0], y[0]))

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, x):
        self.q.insert(x)

    def dequeue(self):
        assert not self.is_empty(), "Queue underflow"
        return self.q.extract_max()

    def __len__(self):
        return len(self.q)

    def __str__(self):
        return f"Queue: front -> {self.q} <- tail"