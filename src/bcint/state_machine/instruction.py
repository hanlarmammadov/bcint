from src.bcint.state_machine.opcodes import Opcodes


class Instruction:

    def __init__(self, operation, operand, offset):
        self._operation = operation
        self._operand = operand
        self._offset = offset

    @property
    def operation(self):
        return self._operation

    @property
    def operand(self):
        return self._operand

    @property
    def offset(self):
        return self._offset

    @property
    def operation_name(self):
        return Opcodes(self._operation).name

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "({offset} {operation_name} {operand})".format(offset=self._offset, operation_name=self.operation_name, operand=self.operand)
