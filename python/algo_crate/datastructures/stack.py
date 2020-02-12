# Stack Data Structure.
# Implements STACK-EMPTY(S), PUSH(S, x), POP(S)
# A stack is a LIFO (last-in first-out) dynamic set structure, where
# the INSERT and DELETE operations are called PUSH and POP respectively.
# Typically implemented using a dynamic array and a stack pointer (though Python
# provides sufficient methods to remove the need for a stack pointer).

# Analysis:
# is_empty (STACK-EMPTY): O(1) (len operation is in constant time O(1))
# push (PUSH): O(1)
# pop (POP): O(1)

# Chapter 10.1, Page 233


from algo_crate.util import is_series


class Stack:

    def __init__(self, *values):

        if not len(values):
            self.s = []
            return

        x = values[0]
        if not is_series(x):
            self.s = [x]
            return

        assert is_series(x)
        assert len(x) > 0

        self.s = list(x)

    def is_empty(self):
        return len(self) == 0

    def push(self, x):
        self.s.append(x)

    def pop(self):
        assert not self.is_empty(), "Stack underflow"
        return self.s.pop()

    def top(self):
        assert not self.is_empty(), "Stack underflow"
        return self.s[-1]

    def __len__(self):
        return len(self.s)

    def __str__(self):
        return f"Stack: {self.s} <- stack pointer"
