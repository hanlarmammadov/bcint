import dis
from src.bcint.state_machine.instruction import Instruction


class OpcodeLoader():
    def __init__(self):
        pass


    def load_from_func(self, func):
        bytecode = dis.Bytecode(func)
        instructions_list = []
        for instr in bytecode:
            instructions_list.append(Instruction(instr.opcode, instr.argval))
        return instructions_list

