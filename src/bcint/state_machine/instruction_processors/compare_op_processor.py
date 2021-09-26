from src.bcint.state_machine.instruction_processors.instruction_processor_base import InstructionProcessorBase
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.heap import Heap
from src.bcint.state_machine.binary_comparer import BinaryComparer


class CompareOpProcessor(InstructionProcessorBase):

    def __init__(self, binary_comparer: BinaryComparer = None):
        if not binary_comparer:
            binary_comparer = BinaryComparer()
        self._binary_comparer = binary_comparer

    def execute(self, operand, func_frame: FuncFrame, func_state: FuncState, heap: Heap):
        value2 = func_frame.eval_stack.pop()
        value1 = func_frame.eval_stack.pop()
        comp_res = self._binary_comparer.compare(operand, value1, value2)
        func_frame.eval_stack.push(comp_res)

    @property
    def binary_comparer(self):
        return self._binary_comparer
