class Node:

    def __init__(self, v):
        self.v = v
        self.next = None

    def __str__(self):
        return f"Node: (v: {self.v}, next: {self.next})"

