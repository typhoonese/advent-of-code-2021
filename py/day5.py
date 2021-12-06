import numpy as np
import re

# read file
filePath = '../data/hydrothermalVent.txt'
coordinatesFile = open(filePath, 'r')
coordinatesLines = coordinatesFile.readlines()

# create a list of all coordinates
coordinates = []
for line in coordinatesLines:
    line = (re.sub(" -> ", ",", line)).strip()
    line = line.split(",")
    line = [int(i) for i in line]
    coordinates.append((line))

cleanedCoordinates = []
for row in coordinates:
    x1 = row[0]
    y1 = row[1]
    x2 = row[2]
    y2 = row[3]
    if (x1 == x2 or y1 == y2 or (abs((y2-y1)/(x2-x1)) == 1)):
        cleanedCoordinates.append(row)
del coordinates

maxVal = -1
for row in cleanedCoordinates:
    for i in range(len(row)):
        if row[i] > maxVal:
            maxVal = row[i]

# Part 1
allCoordinates = []
for row in cleanedCoordinates:
    x1 = row[0]
    y1 = row[1]
    x2 = row[2]
    y2 = row[3]
    coordinateSystem = np.zeros((maxVal+1, maxVal+1))
    # horizontal lines
    if (x1 == x2 and y1 != y2):
        for i in range(min(y1, y2), max(y1, y2)+1):
            coordinateSystem[i][x1] = 1
    # vertical lines
    elif (y1 == y2 and x1 != x2):
        for i in range(min(x1, x2), max(x1, x2)+1):
            coordinateSystem[y1][i] = 1
    # positive slope x1=y1
    elif x1 == y1 and x2 == y2:
        for i in range(max(x1, x2)-min(x1, x2)+1):
            coordinateSystem[min(y1, y2)+i][min(x1, x2)+i] = 1
    # positive slope
    elif (y2-y1)/(x2-x1) == 1:
        for i in range(max(x1, x2) - min(x1, x2)+1):
            coordinateSystem[min(y1, y2)+i][min(x1, x2)+i] = 1
    # negative slope
    elif (y2-y1)/(x2-x1) == -1:
        for i in range(abs(x1-x2)+1):
            tempX = min(x1, x2)
            tempY = -1
            if tempX == x1:
                tempY = y1
            else:
                tempY = y2
            coordinateSystem[tempY-i][tempX+i] = 1
    else:
        print("\nUnexpected")
        print(x1, x2, y1, y2)
    allCoordinates.append(coordinateSystem)

# sum all coordinates
ventMap = np.zeros((maxVal+1, maxVal+1))
for matrix in allCoordinates:
    ventMap += matrix

# count the points (x, y) that are > 1
total = 0
for row in range(maxVal+1):
    for column in range(maxVal+1):
        if ventMap[row][column] > 1:
            total += 1

print("Total score: ", total)
