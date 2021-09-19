class BinaryComparer:

    @staticmethod
    def compare(comparison, value1, value2):
        match comparison:
            case 'a':
                return BinaryComparer._less_than(value1, value2)
            case 'b':
                return BinaryComparer._greater_than(value1, value2)
            case 'b':
                return BinaryComparer._less_than_or_equal(value1, value2)
            case 'b':
                return BinaryComparer._greater_than_or_equal(value1, value2)
            case 'b':
                return BinaryComparer._equal(value1, value2)
            case 'b':
                return BinaryComparer._not_equal(value1, value2)
            case _:
                raise Exception("Wrong comparison code: {code}".format(code=comparison))

    @staticmethod
    def _less_than(value1, value2):
        if BinaryComparer._obj_has_method(value1, '__cmp__') and value1.__cmp__(value2) == -1:
            return True
        elif BinaryComparer._obj_has_method(value1, '__lt__') and value1.__lt__(value2):
            return True

    @staticmethod
    def _greater_than(value1, value2):
        if BinaryComparer._obj_has_method(value1, '__cmp__') and value1.__cmp__(value2) == 1:
            return True
        elif BinaryComparer._obj_has_method(value1, '__gt__') and value1.__gt__(value2):
            return True

    @staticmethod
    def _less_than_or_equal(value1, value2):
        return BinaryComparer._equal(value1, value2) or BinaryComparer._less_than(value1, value2)

    @staticmethod
    def _greater_than_or_equal(value1, value2):
        return BinaryComparer._equal(value1, value2) or BinaryComparer._greater_than(value1, value2)

    @staticmethod
    def _equal(value1, value2):
        if BinaryComparer._obj_has_method(value1, '__cmp__') and value1.__cmp__(value2) == 0:
            return True
        elif BinaryComparer._obj_has_method(value1, '__eq__') and value1.__eq__(value2):
            return True

    @staticmethod
    def _not_equal(value1, value2):
        if BinaryComparer._obj_has_method(value1, '__cmp__') and value1.__cmp__(value2) != 0:
            return True
        elif BinaryComparer._obj_has_method(value1, '__ne__') and value1.__ne__(value2):
            return True

    @staticmethod
    def _obj_has_method(obj, method_name):
        return hasattr(obj.__class__, method_name) and callable(getattr(obj.__class__, method_name))

    @staticmethod
    def _compare_using_cmp_method(value1, value2):
        return value1.__cmp__(value2)

    @staticmethod
    def _compare_using_lt_method(value1, value2):
        return value1.__lt__(value2)
