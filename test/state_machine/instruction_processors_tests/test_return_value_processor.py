import pytest
from src.bcint.state_machine.instruction_processors.return_value_processor import ReturnValueProcessor
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
    func_state = FuncState(1)

    # Act
    ReturnValueProcessor.execute(None, func_frame, func_state, Heap())

    # Assert
    assert eval_stack.length == 0
    assert locals_dict.length == 0
    assert func_state.returned_value == 42


def test_execute_with_two_values_on_stack():
    # Arrange
    eval_stack = EvalStack()
    eval_stack.push(42)
    eval_stack.push(43)
    locals_dict = Locals()
    func_frame = FuncFrame(eval_stack, locals_dict)
    func_state = FuncState(1)

    # Act
    with pytest.raises(Exception) as ex:
        ReturnValueProcessor.execute(None, func_frame, func_state, [])
