def beenToSameSmallCave(path):
    pathLastIndex = len(path)-2
    lastCave = path[pathLastIndex:]
    found = path[0:pathLastIndex-2].find(lastCave)
    if found == -1:
        return 0, path
    else:
        return 1, path[0:pathLastIndex]


def checkIfSmallCave(cave):  # cave is the letter(s) representing the cave
    isSmallCave = 1
    isBigCave = 0
    if ord(cave[0]) >= 97 and ord(cave[0]) <= 122:
        return isSmallCave
    return isBigCave


def makePath(path, nextStop):
    if nextStop == 'end':
        possiblePaths.append(path)
    # if the next cave is a big cave
    elif not checkIfSmallCave(nextStop):
        path += nextStop
        nextStops = paths[nextStop]
        for stop in nextStops:
            makePath(path, stop)
    # if the next cave is a small cave, check if been before
    elif checkIfSmallCave(nextStop):
        if nextStop not in paths:
            return 0
        path += nextStop
        (beenToCave, path) = beenToSameSmallCave(path)
        if not beenToCave:
            nextStops = paths[nextStop]
            for stop in nextStops:
                makePath(path, stop)
        else:
            return 0


# read file
sourcePath = '../data/passage.txt'
passageFile = open(sourcePath, 'r')
passageLines = passageFile.readlines()

paths = {}  # dictionary of possible connections
possiblePaths = []  # possible paths that go to the end cave
for line in passageLines:
    line = tuple(line.strip().split('-'))

    connection1 = line[0]
    connection2 = line[1]

    if connection1 == 'end':
        if connection2 not in paths:
            paths[connection2] = []
        paths[connection2].append(connection1)
    elif connection1 == 'start':
        if connection1 not in paths:
            paths[connection1] = []
        paths[connection1].append(connection2)
    elif connection2 == 'start':
        if connection2 not in paths:
            paths[connection2] = []
        paths[connection2].append(connection1)
    elif connection2 == 'end':
        if connection1 not in paths:
            paths[connection1] = []
        paths[connection1].append(connection2)
    else:
        if connection1 not in paths:
            paths[connection1] = []
        if connection2 not in paths:
            paths[connection2] = []
        paths[connection1].append(connection2)
        paths[connection2].append(connection1)

firstStop = 'start'
path = ''
for nextStop in paths[firstStop]:
    makePath(path, nextStop)
print("Paths found:", len(possiblePaths))
