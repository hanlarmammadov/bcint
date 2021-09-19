from src.bcint.state_machine.instruction_processors.instruction_processor_base import InstructionProcessorBase
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.heap import Heap


class CompareOpProcessor(InstructionProcessorBase):

    @staticmethod
    def execute(operand, func_frame: FuncFrame, func_state: FuncState, heap: Heap):
        value2 = func_frame.eval_stack.pop()
        value1 = func_frame.eval_stack.pop()
        match operand:
            case 'a':
                return 1
            case 'b':
                return 2
            case _:
                return 0  # 0 is the default case if x is not found
