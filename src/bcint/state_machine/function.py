import string


class Function:

    def __init__(self, name: string, instructions: list):
        self._name = name
        self._instructions = instructions

    @property
    def name(self):
        return self._name

    @property
    def instructions(self):
        return self._instructions
   