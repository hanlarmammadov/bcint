from enum import Enum


class FlowInterruption(Enum):
    NONE = 0,
    CALL = 1,
    RETURN = 2,
    THROW = 3,
    FINISHED = 4

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
