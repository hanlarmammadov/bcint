from src.bcint.state_machine.eval_stack import EvalStack
from src.bcint.state_machine.locals import Locals


class FuncFrame:

    def __init__(self, eval_stack: EvalStack, locals_dict: Locals):
        self.eval_stack = eval_stack
        self.locals_dict = locals_dict
