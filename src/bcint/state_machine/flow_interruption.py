from enum import Enum


class FlowInterruption(Enum):
    NONE = 0,
    CALL = 1,
    RETURN = 2,
    THROW = 3,
    FINISHED = 4
