from src.bcint.state_machine.instruction_processors.instruction_processor_base import InstructionProcessorBase


class LoadFastProcessor(InstructionProcessorBase):

    @staticmethod
    def execute(operand, func_frame, func_state, gc_heap):
        func_frame.eval_stack.push(func_frame.locals_dict.load(operand))