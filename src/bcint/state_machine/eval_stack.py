class EvalStack:

    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        l = len(self._stack)
        if l != 0:
            return self._stack[l - 1]

    @property
    def length(self):
        return len(self._stack)

    @property
    def contains(self):
        return len(self._stack) != 0
