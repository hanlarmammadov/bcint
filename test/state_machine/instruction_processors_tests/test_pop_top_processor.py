from src.bcint.state_machine.instruction_processors.pop_top_processor import PopTopProcessor
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.eval_stack import EvalStack
from src.bcint.state_machine.locals import Locals
from src.bcint.state_machine.heap import Heap


def test_execute():
    # Arrange
    eval_stack = EvalStack()
    eval_stack.push(42)
    locals_dict = Locals()
    func_frame = FuncFrame(eval_stack, locals_dict)
    pop_top = PopTopProcessor()

    # Act
    pop_top.execute(None, func_frame, FuncState(1), Heap())

    # Assert
    assert eval_stack.length == 0
    assert locals_dict.length == 0


def test_execute_with_two_values_on_stack():
    # Arrange
    eval_stack = EvalStack()
    eval_stack.push(42)
    eval_stack.push(43)
    locals_dict = Locals()
    func_frame = FuncFrame(eval_stack, locals_dict)
    pop_top = PopTopProcessor()

    # Act
    pop_top.execute(None, func_frame, FuncState(1), Heap())

    # Assert
    assert eval_stack.length == 1
    assert eval_stack.pop() == 42
    assert locals_dict.length == 0
