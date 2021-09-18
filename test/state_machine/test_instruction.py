from src.bcint.state_machine.instruction import Instruction
from src.bcint.state_machine.opcodes import Opcodes


def test_initialization():
    # Arrange
    operation = 100
    operand = 'print'
    # Act
    inst = Instruction(operation, operand)
    # Assert
    assert inst.operation == 100
    assert inst.operand == 'print'


def test_instruction_name():
    # Arrange
    opcode = Opcodes.LOAD_GLOBAL
    inst = Instruction(opcode, 'print')
    # Act
    name = inst.operation_name
    # Assert
    assert name == 'LOAD_GLOBAL'


def test_repr():
    # Arrange
    opcode = Opcodes.LOAD_GLOBAL
    inst = Instruction(opcode, 'print')
    # Act
    repr_actual = inst.__repr__()
    # Assert
    assert repr_actual == '(LOAD_GLOBAL print)'


def test_str():
    # Arrange
    opcode = Opcodes.LOAD_GLOBAL
    inst = Instruction(opcode, 'print')
    # Act
    str_actual = inst.__str__()
    # Assert
    assert str_actual == '(LOAD_GLOBAL print)'


def test_str_are_equal_to_repr():
    # Arrange
    opcode = Opcodes.LOAD_GLOBAL
    inst = Instruction(opcode, 'print')

    # Assert
    assert inst.__str__() == inst.__repr__()

