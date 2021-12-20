def beenToSameSmallCave(path):
    pathLastIndex = len(path)-1
    lastCave = path[pathLastIndex]
    found = path[0:pathLastIndex].find(lastCave)
    if found == -1:
        return 0, path
    else:
        return 1, path[0:pathLastIndex]


def makePath(path, nextStop):
    if nextStop == 'end':
        possiblePaths.append(path)
    # if the next cave is a big cave
    elif ord(nextStop) >= 65 and ord(nextStop) <= 90:
        path += nextStop
        nextStops = paths[nextStop]
        for stop in nextStops:
            makePath(path, stop)
    # if the next cave is a small cave, check if been before
    elif ord(nextStop) >= 97 and ord(nextStop) <= 122:
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

paths = {}
possiblePaths = []
for line in passageLines:
    line = tuple(line.strip().split('-'))
    if line[0] not in paths:
        paths[line[0]] = []
    paths[line[0]].append(line[1])

    # if line is A -> b, map b -> A as from b can be returned to A
    if len(line[0]) == 1 and len(line[1]) == 1 and ord(line[0]) >= 65 and ord(line[0]) <= 90:
        if line[1] not in paths:
            paths[line[1]] = []
        paths[line[1]].append(line[0])

print("PATHS:", paths)

firstStop = 'start'
path = ''
for nextStop in paths[firstStop]:
    makePath(path, nextStop)

print("Paths found:", len(possiblePaths))
for path in possiblePaths:
    print("\nPath:", path)
