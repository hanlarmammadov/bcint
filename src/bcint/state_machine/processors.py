from src.bcint.state_machine.opcodes import Opcodes
from src.bcint.state_machine.instruction_processors.binary_add_processor import BinaryAddProcessor
from src.bcint.state_machine.instruction_processors.load_const_processor import LoadConstProcessor
from src.bcint.state_machine.instruction_processors.load_fast_processor import LoadFastProcessor
from src.bcint.state_machine.instruction_processors.pop_top_processor import PopTopProcessor
from src.bcint.state_machine.instruction_processors.store_fast_processor import StoreFastProcessor
from src.bcint.state_machine.instruction_processors.return_value_processor import ReturnValueProcessor
from src.bcint.state_machine.instruction_processors.compare_op_processor import CompareOpProcessor


class Processors:

    def __init__(self):
        self._dict = {
            int(Opcodes.BINARY_ADD): BinaryAddProcessor(),
            int(Opcodes.LOAD_CONST): LoadConstProcessor(),
            int(Opcodes.LOAD_FAST): LoadFastProcessor(),
            int(Opcodes.POP_TOP): PopTopProcessor(),
            int(Opcodes.STORE_FAST): StoreFastProcessor(),
            int(Opcodes.RETURN_VALUE): ReturnValueProcessor(),
            int(Opcodes.COMPARE_OP): ReturnValueProcessor()
        }

    def get(self, opcode):
        return self._dict[opcode]
