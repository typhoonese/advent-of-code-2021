import numpy as np


def markPoint(matrix, point, value):
    matrix[point[1]][point[0]] = value
    return matrix


def fold(matrix, instruction):
    shape = matrix.shape
    if instruction[0] == "y":
        for y in range(instruction[1]+1, shape[0]):
            for x in range(shape[1]):
                if matrix[y][x] == 1:
                    matrix[y-(y-instruction[1])*2][x] = 1
        matrix = matrix[0:instruction[1], :]
    elif instruction[0] == "x":
        for y in range(shape[0]):
            for x in range(instruction[1]+1, shape[1]):
                if matrix[y][x] == 1:
                    matrix[y][x-(x-instruction[1])*2] = 1
        matrix = matrix[:, 0:instruction[1]]
    else:
        print("unexpected")
        return 0
    return matrix


def findTotal(matrix):
    totalSum = 0
    shape = matrix.shape
    for y in range(shape[0]):
        for x in range(shape[1]):
            totalSum += matrix[y][x]
    return int(totalSum)


def printMatrix(matrix):
    shape = matrix.shape
    for y in range(shape[0]):
        row = ""
        for x in range(shape[1]):
            if matrix[y][x] == 0:
                row += " "
            elif matrix[y][x] == 1:
                row += ("*")
        print(row)


# read file
sourcePath = '../data/manual.txt'
manualFile = open(sourcePath, 'r')
manualLines = manualFile.readlines()

coordinates = []
foldingRules = []
highestX = 0
highestY = 0
ruleIndex = 11
for line in manualLines:
    isRule = 0
    if line.find("fold along") != -1:
        isRule = 1
    if line == "\n":
        continue
    elif not isRule:
        line = line.strip().split(',')
        line = [int(i) for i in line]
        highestX = max(highestX, line[0])
        highestY = max(highestY, line[1])
        coordinates.append(tuple(line))
    elif isRule:
        line = line[ruleIndex:]
        line = line.strip().split('=')
        line[1] = int(line[1])
        foldingRules.append(tuple(line))

# create a matrix of the transparent paper
transparentPaper = np.zeros((highestY+1, highestX+1))

for coordinate in coordinates:
    transparentPaper = markPoint(transparentPaper, coordinate, 1)

for instruction in foldingRules:
    transparentPaper = fold(transparentPaper, instruction)
    print(findTotal(transparentPaper))

printMatrix(transparentPaper)
