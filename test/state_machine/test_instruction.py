from src.bcint.state_machine.instruction import Instruction
from src.bcint.state_machine.opcodes import Opcodes


def test_initialization():
    # Arrange
    operation = 100
    operand = 'print'
    # Act
    inst = Instruction(operation, operand, 0)
    # Assert
    assert inst.operation == 100
    assert inst.operand == 'print'
    assert inst.operation_name == 'LOAD_CONST'
    assert inst.offset == 0


def test_repr():
    # Arrange
    opcode = Opcodes.LOAD_GLOBAL
    inst = Instruction(opcode, 'print', 0)
    # Act
    repr_actual = inst.__repr__()
    # Assert
    assert repr_actual == '(0 LOAD_GLOBAL print)'


def test_str_are_equal_to_repr():
    # Arrange
    opcode = Opcodes.LOAD_GLOBAL
    inst = Instruction(opcode, 'print', 0)

    # Assert
    assert inst.__str__() == inst.__repr__()

