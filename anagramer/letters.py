from models.letter import Letter


def parseLine(line):
    letters = []
    for linePart in line.split(","):
        lpp = linePart.replace(" ", "")
        letterName = lpp[lpp.find("x") - 2]
        letterAmount = lpp[lpp.find("x") + 1]
        letterValue = lpp[0]
        letters.append(Letter(letterName, letterAmount, letterValue))
    return letters


def ReadDoc():
    letterBag = []
    file = open("assets/wiki.txt")
    f1 = file.readlines()

    for line in f1:
        for item in parseLine(line):
            letterBag += [item]
    return letterBag


print(ReadDoc()[0].name)
for item in ReadDoc():
    print(item.name)

