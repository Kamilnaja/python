from enum import Enum

class State(Enum):
    NOT_FOUND = 0  # no match between searched and generated
    FOUND = 1  # found one or more
    ALL_EQUALS = 2  # all ok
    STR_GENERATED = 3
    NONE_EQUAL = 4  # none match
    PARTIALY_EQUAL = 5  # some match

searched = "lo"
tempSearched = []