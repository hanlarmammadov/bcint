from src.bcint.state_machine.instruction_processors.instruction_processor_base import InstructionProcessorBase


class BinaryAddProcessor(InstructionProcessorBase):

    @staticmethod
    def execute(operand, func_frame, func_state, gc_heap):
        value1 = func_frame.eval_stack.pop()
        value2 = func_frame.eval_stack.pop()
        func_frame.eval_stack.push(value1 + value2)
