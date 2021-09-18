class Locals:

    def __init__(self):
        self._dict = {}

    def save(self, cell, value):
        self._dict[cell] = value

    def load(self, cell):
        return self._dict[cell]

    @property
    def length(self):
        return len(self._dict)
