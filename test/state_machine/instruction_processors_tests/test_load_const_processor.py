from src.bcint.state_machine.instruction_processors.load_const_processor import LoadConstProcessor
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.eval_stack import EvalStack
from src.bcint.state_machine.locals import Locals
from src.bcint.state_machine.heap import Heap

def test_execute():
    # Arrange
    eval_stack = EvalStack()
    locals_dict = Locals()
    func_frame = FuncFrame(eval_stack, locals_dict)
    load_const = LoadConstProcessor()

    # Act
    load_const.execute(4, func_frame, FuncState(1), Heap())

    # Assert
    assert eval_stack.length == 1
    assert eval_stack.pop() == 4
    assert locals_dict.length == 0

