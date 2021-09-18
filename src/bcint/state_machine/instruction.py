from src.bcint.state_machine.opcodes import Opcodes


class Instruction:

    def __init__(self, operation, operand):
        self._operation = operation
        self._operand = operand

    @property
    def operation(self):
        return self._operation

    @property
    def operand(self):
        return self._operand

    @property
    def operation_name(self):
        return Opcodes(self._operation).name

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "({operation_name} {operand})".format(operation_name=self.operation_name, operand=self.operand)
