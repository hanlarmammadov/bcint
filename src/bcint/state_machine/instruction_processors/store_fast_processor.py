from src.bcint.state_machine.instruction_processors.instruction_processor_base import InstructionProcessorBase


class StoreFastProcessor(InstructionProcessorBase):

    @staticmethod
    def execute(operand, func_frame, func_state, gc_heap):
        value = func_frame.eval_stack.pop()
        func_frame.locals_dict.save(operand, value)

