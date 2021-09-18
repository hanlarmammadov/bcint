from src.bcint.state_machine.func_state import FuncState
from src.bcint.state_machine.flow_interruption import FlowInterruption


def test_initialization():
    # Act
    func_state = FuncState(5)

    # Assert
    assert func_state.curr_index == -1
    assert func_state.jump_index == -1
    assert func_state.num_of_ins == 5
    assert func_state.flow_interruption == FlowInterruption.NONE
    assert func_state.returned_value is None


def test_repr():
    # Arrange
    func_state = FuncState(5)

    # Act
    repr_actual = func_state.__repr__()

    # Assert
    assert repr_actual == 'ind: -1 jmp: -1 len: 5 intr: NONE ret: None'


def test_str_are_equal_to_repr():
    # Arrange
    func_state = FuncState(5)

    # Assert
    assert func_state.__str__() == func_state.__repr__()
