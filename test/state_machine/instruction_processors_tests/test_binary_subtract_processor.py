from src.bcint.state_machine.instruction_processors.binary_subtract_processor import BinarySubtractProcessor
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.eval_stack import EvalStack
from src.bcint.state_machine.locals import Locals
from src.bcint.state_machine.heap import Heap


def test_execute():
    # Arrange
    eval_stack = EvalStack()
    eval_stack.push(10)
    eval_stack.push(8)
    locals_dict = Locals()
    func_frame = FuncFrame(eval_stack, locals_dict)
    binary_subtract = BinarySubtractProcessor()

    # Act
    binary_subtract.execute(None, func_frame, FuncState(1), Heap())

    # Assert
    assert eval_stack.length == 1
    assert eval_stack.pop() == 2
    assert locals_dict.length == 0

