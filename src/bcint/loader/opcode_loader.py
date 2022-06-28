import dis
from src.bcint.state_machine.instruction import Instruction


class OpcodeLoader():
    _jump_instruction_codes = [110, 111, 112, 113, 114, 115, 121, 40]  # JUMP_FORWARD(110), JUMP_IF_FALSE_OR_POP (111), JUMP_IF_TRUE_OR_POP (112), JUMP_ABSOLUTE (113), POP_JUMP_IF_FALSE (114), POP_JUMP_IF_TRUE (115), JUMP_IF_NOT_EXC_MATCH (121), JUMP_ABSOLUTE_QUICK (40)

    def __init__(self):
        pass

    def load_from_func(self, func):
        bytecode = dis.Bytecode(func)
        instructions_list = []
        for instr in bytecode:
            instructions_list.append(Instruction(instr.opcode, instr.argval, instr.offset))

        # Fix jump addresses
        for instr in instructions_list:
            if instr in _jump_instruction_codes:
                _fix_jump_address(instruction, instructions_list)

        return instructions_list

    def _fix_jump_address(jump_instr: Instruction, instructions_list: []):
        offset = jump_instr.offset
        jump_index = -1
        for index, instr in enumerate(instructions_list):
            if instr.offset == offset:
                jump_index = index
                break
        if jump_index == -1:
            raise Error("Jump index for this offset not found")
        jump_instr.operand = jump_index
