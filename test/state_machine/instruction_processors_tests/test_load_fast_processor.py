from src.bcint.state_machine.instruction_processors.load_fast_processor import LoadFastProcessor
from src.bcint.state_machine.func_frame import FuncFrame
from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.eval_stack import EvalStack
from src.bcint.state_machine.locals import Locals


def test_execute():
    # Arrange
    eval_stack = EvalStack()
    locals_dict = Locals()
    locals_dict.save('a', 42)
    func_frame = FuncFrame(eval_stack, locals_dict)

    # Act
    LoadFastProcessor.execute('a', func_frame, FuncState(1), [])

    # Assert
    assert eval_stack.length == 1
    assert eval_stack.pop() == 42
    assert locals_dict.length == 1
    assert locals_dict.load('a') == 42

