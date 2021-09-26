from src.bcint.state_machine.instruction_processors.compare_op_processor import CompareOpProcessor
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.eval_stack import EvalStack
from src.bcint.state_machine.locals import Locals
from src.bcint.state_machine.heap import Heap
import unittest.mock as mk


def test_ctor__when_binary_comparer_not_provided__then_init_default_one():
    compare_op = CompareOpProcessor()
    assert compare_op.binary_comparer is not None
    assert type(compare_op.binary_comparer)


def test_ctor__when_binary_comparer_provided__then_init_default_one():
    custom_binary_comparer = mk.Mock()
    compare_op = CompareOpProcessor(custom_binary_comparer)
    assert compare_op.binary_comparer is not None
    assert custom_binary_comparer == compare_op.binary_comparer


def test_execute__when_called__then_uses_binary_comparer_to_compare():
    # Arrange
    binary_comparer_mock = mk.Mock()
    binary_comparer_mock.compare = mk.MagicMock(return_value=True)
    value1 = 42
    value2 = 43
    eval_stack = EvalStack()
    eval_stack.push(value1)
    eval_stack.push(value2)
    locals_dict = Locals()
    func_frame = FuncFrame(eval_stack, locals_dict)
    compare_op = CompareOpProcessor(binary_comparer_mock)

    # Act
    compare_op.execute('<', func_frame, FuncState(1), Heap())

    # Assert
    binary_comparer_mock.compare.assert_called_once_with('<', value1, value2)
    assert eval_stack.length == 1
    assert locals_dict.length == 0
    assert eval_stack.pop() is True
