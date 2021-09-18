from src.bcint.loader import opcode_loader
from src.bcint.state_machine.opcodes import Opcodes


def test_instructions_loaded_correctly():
    # Arrange
    def function():
        a = 3
        b = 4
        c = a + b
        return c
    loader = opcode_loader.OpcodeLoader()

    # Act
    instr_list = loader.load_from_func(function)

    # Assert
    assert len(instr_list) == 10
    assert instr_list[0].operation == int(Opcodes.LOAD_CONST)
    assert instr_list[0].operand == 3
    assert instr_list[1].operation == int(Opcodes.STORE_FAST)
    assert instr_list[1].operand == 'a'
    assert instr_list[2].operation == int(Opcodes.LOAD_CONST)
    assert instr_list[2].operand == 4
    assert instr_list[3].operation == int(Opcodes.STORE_FAST)
    assert instr_list[3].operand == 'b'
    assert instr_list[4].operation == int(Opcodes.LOAD_FAST)
    assert instr_list[4].operand == 'a'
    assert instr_list[5].operation == int(Opcodes.LOAD_FAST)
    assert instr_list[5].operand == 'b'
    assert instr_list[6].operation == int(Opcodes.BINARY_ADD)
    assert instr_list[6].operand is None
    assert instr_list[7].operation == int(Opcodes.STORE_FAST)
    assert instr_list[7].operand == 'c'
    assert instr_list[8].operation == int(Opcodes.LOAD_FAST)
    assert instr_list[8].operand == 'c'
    assert instr_list[9].operation == int(Opcodes.RETURN_VALUE)
    assert instr_list[9].operand is None
