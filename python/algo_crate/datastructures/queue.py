from algo_crate.util import is_series


class Queue:

    def __init__(self, *values):

        if not len(values):
            self.q = []
            return

        x = values[0]
        if not is_series(x):
            self.q = [x]
            return

        assert is_series(x)
        assert len(x) > 0

        self.q = list(x)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, x):
        self.q.insert(0, x)

    def dequeue(self):
        assert not self.is_empty(), "Queue underflow"
        return self.q.pop()

    def __len__(self):
        return len(self.q)

    def __str__(self):
        return f"Queue: front -> {self.q} <- tail"