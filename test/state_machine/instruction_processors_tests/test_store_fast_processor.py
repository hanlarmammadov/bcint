from src.bcint.state_machine.instruction_processors.store_fast_processor import StoreFastProcessor
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
    store_fast = StoreFastProcessor()

    # Act
    store_fast.execute('a', func_frame, FuncState(1), Heap())

    # Assert
    assert eval_stack.length == 0
    assert locals_dict.length == 1
    assert locals_dict.load('a') == 42

