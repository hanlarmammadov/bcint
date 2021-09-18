from src.bcint.state_machine.function import Function
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.eval_stack import EvalStack
from src.bcint.state_machine.locals import Locals
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.flow_interruption import FlowInterruption
from src.bcint.state_machine.processors import Processors
from src.bcint.state_machine.heap import Heap


class FuncStateMachine:

    def __init__(self, func: Function, processors: Processors, heap: Heap):
        self._func_name = func.name
        self._instructions = func.instructions
        self._func_frame = self._create_new_frame()
        self._func_state = FuncState(len(func.instructions))
        self._heap = heap
        self._processors = processors

    def execute(self):
        try:
            while self._func_state.flow_interruption == FlowInterruption.NONE:
                next_index = self.get_next_instruction_index()
                if next_index == -1:
                    self._func_state.flow_interruption = FlowInterruption.FINISHED
                    break
                # get instruction processor and run instruction
                instruction = self._instructions[next_index]
                processor = self._processors.get(instruction.operation)
                processor.execute(instruction.operand, self._func_frame, self._func_state, self._heap)
        except Exception as e:
            raise

    def get_next_instruction_index(self):
        index = -1
        if self._func_state.jump_index != -1:
            self._func_state.curr_index = self._func_state.jump_index
            self._func_state.jump_index = -1
            index = self._func_state.curr_index
        elif self._func_state.curr_index < self._func_state.num_of_ins - 1:
            self._func_state.curr_index += 1
            index = self._func_state.curr_index
        return index

    @staticmethod
    def _create_new_frame():
        eval_stack = EvalStack()
        locals_dict = Locals()
        func_frame = FuncFrame(eval_stack, locals_dict)
        return func_frame

    @property
    def func_name(self):
        return self._func_name

    @property
    def func_frame(self):
        return self._func_frame

    @property
    def func_state(self):
        return self._func_state
