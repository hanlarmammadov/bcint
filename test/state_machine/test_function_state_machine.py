from src.bcint.loader.opcode_loader import OpcodeLoader
from src.bcint.state_machine.func_state_machine import FuncStateMachine
from src.bcint.state_machine.function import Function
from src.bcint.state_machine.processors import Processors
from src.bcint.state_machine.heap import Heap


def test_return_integer():
    # Arrange
    def function():
        a = 42
        return a
    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned == 42


def test_add_integer_constants_and_return_result():
    # Arrange
    def function():
        return 5+6+7

    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned == 18


def test_add_two_integer_variables_and_return_result():
    # Arrange
    def function():
        a = 1
        b = 2
        c = a + b
        return c

    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned == 3


def test_load_multiple_values_and_return_one():
    # Arrange
    def function():
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        return c

    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned == 3


def test_multiple_int_assignations():
    # Arrange
    def function():
        a = 1
        a = 2
        a = 5
        return a

    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned == 5


def test_multiple_int_assignations_2():
    # Arrange
    def function():
        a = 1
        b = a
        return b

    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned == 1


def test_function_that_returns_none():
    # Arrange
    def function():
        a = 1
        b = 5
        c = 7

    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned is None


def test_function_that_returns_none():
    # Arrange
    def function():
        1 + 5

    loader = OpcodeLoader()
    instr_list = loader.load_from_func(function)
    function = Function("test_function", instr_list)
    func_sm = FuncStateMachine(function, Processors(), Heap())

    # Act
    func_sm.execute()

    # Assert
    returned = func_sm.func_state.returned_value
    assert returned is None
