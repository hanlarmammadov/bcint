from src.bcint.state_machine.instruction_processors.instruction_processor_base import InstructionProcessorBase
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.heap import Heap


class LoadConstProcessor(InstructionProcessorBase):

    def execute(self, operand, func_frame: FuncFrame, func_state: FuncState, heap: Heap):
        func_frame.eval_stack.push(operand)
