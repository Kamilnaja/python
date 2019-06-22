from generator import Generator
from state import State


class Comparator:
    temporarySearchedReplacement = ""

    @staticmethod
    def compareRandomWithSearched(searched, random):
        print("random: " + random + " searched: " + searched)

        if "".join(searched) == Generator.generateResponseTable(searched):
            return [State.ALL_EQUALS, False]
        else:
            temporarySearchedReplacement = []
            randomIterator = iter(random)

            for x in searched:
                if x == "_":
                    temporarySearchedReplacement.append("_")
                else:
                    if x == next(randomIterator):
                        print("random: " + random + " searched: " + searched)
                        print("equal: " + x)
                        temporarySearchedReplacement.append("_")
                    else:
                        temporarySearchedReplacement.append(x)

            return [State.PARTIALY_EQUAL, temporarySearchedReplacement]
