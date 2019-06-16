from enum import Enum

class State(Enum):
    NOT_FOUND = 0  # no match between searched and generated
    FOUND = 1  # found one or more
    ALL_EQUALS = 2  # all ok
    NONE_EQUAL = 3  # none match
    PARTIALY_EQUAL = 4  # some match

tempSearched = []