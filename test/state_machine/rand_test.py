from src.bcint.loader.opcode_loader import OpcodeLoader
from src.bcint.state_machine.func_state_machine import FuncStateMachine
from src.bcint.state_machine.function import Function
from src.bcint.state_machine.processors import Processors
from src.bcint.state_machine.heap import Heap
import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_return_integer():
    # Arrange
    def function():
        a = 42
        if a == 42:
            return 1
        else:
            return 2

    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned == 42

#(LOAD_CONST 42)
#(STORE_FAST a)
#(LOAD_FAST a)
#(LOAD_CONST 42)
#(COMPARE_OP ==)
#(POP_JUMP_IF_FALSE 16)
#(LOAD_CONST 1)
#(RETURN_VALUE None)
#(LOAD_CONST 2)
#(RETURN_VALUE None)
#(LOAD_CONST None)
#(RETURN_VALUE None)