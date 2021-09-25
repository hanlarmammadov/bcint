from src.bcint.state_machine.binary_comparer import BinaryComparer
import unittest.mock as mk


class EmptyClass:
    pass


class ClassWithCmpMethod:

    def __cmp__(self, other):
        pass


class ClassWithLtMethod:

    def __lt__(self, other):
        pass


def test__less_than__when_cmp_defined__then_uses_cmp_1():
    object1 = ClassWithCmpMethod()
    object2 = EmptyClass()
    object1.__cmp__ = mk.MagicMock(return_value=-1)
    object1.__lt__ = mk.MagicMock()

    is_less = BinaryComparer._less_than(object1, object2)

    assert is_less
    object1.__cmp__.assert_called_once_with(object2)
    object1.__lt__.assert_not_called()


def test__less_than__when_cmp_defined__then_uses_cmp_2():
    object1 = ClassWithCmpMethod()
    object2 = EmptyClass()
    object1.__cmp__ = mk.MagicMock(return_value=0)
    object1.__lt__ = mk.MagicMock()

    is_less = BinaryComparer._less_than(object1, object2)

    assert not is_less
    object1.__cmp__.assert_called_once_with(object2)
    object1.__lt__.assert_not_called()


def test__less_than__when_cmp_defined__then_uses_cmp_3():
    object1 = ClassWithCmpMethod()
    object2 = EmptyClass()
    object1.__cmp__ = mk.MagicMock(return_value=1)
    object1.__lt__ = mk.MagicMock()

    is_less = BinaryComparer._less_than(object1, object2)

    assert not is_less
    object1.__cmp__.assert_called_once_with(object2)
    object1.__lt__.assert_not_called()


def test__less_than__when_lt_defined__then_uses_lt_1():
    object1 = ClassWithLtMethod()
    object2 = EmptyClass()
    object1.__lt__ = mk.MagicMock(return_value=True)
    object1.__cmp__ = mk.MagicMock()

    is_less = BinaryComparer._less_than(object1, object2)

    assert is_less
    object1.__lt__.assert_called_once_with(object2)
    object1.__cmp__.assert_not_called()


def test__less_than__when_lt_defined__then_uses_lt_2():
    object1 = ClassWithLtMethod()
    object2 = EmptyClass()
    object1.__lt__ = mk.MagicMock(return_value=False)
    object1.__cmp__ = mk.MagicMock()

    is_less = BinaryComparer._less_than(object1, object2)

    assert not is_less
    object1.__lt__.assert_called_once_with(object2)
    object1.__cmp__.assert_not_called()

# TODO: tests for other methods
