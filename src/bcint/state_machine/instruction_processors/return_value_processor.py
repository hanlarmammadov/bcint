from src.bcint.state_machine.instruction_processors.instruction_processor_base import InstructionProcessorBase
from src.bcint.state_machine.flow_interruption import FlowInterruption
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.heap import Heap


class ReturnValueProcessor(InstructionProcessorBase):

    def execute(self, operand, func_frame: FuncFrame, func_state: FuncState, heap: Heap):
        if func_frame.eval_stack.length != 1:
            raise Exception('At this point the evaluation stack should contain a single value that is supposed to be returned')
        func_state.flow_interruption = FlowInterruption.RETURN
        func_state.returned_value = func_frame.eval_stack.pop()
