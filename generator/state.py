from enum import Enum

class State(Enum):
    ALL_EQUALS = 0  # all ok
    NONE_EQUAL = 1  # none match
    PARTIALY_EQUAL = 2  # some match
