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
    if (row[0] == row[2] or row[1] == row[3]):
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
    coordinateSystem = np.zeros((maxVal+1, maxVal+1))
    for i in range(len(row)):
        # vertical lines
        if (row[0] == row[2]):
            for i in range(min(row[1], row[3]), max(row[1], row[3])+1):
                coordinateSystem[row[0]][i] = 1
        # horizontal lines
        elif (row[1] == row[3]):
            for i in range(min(row[0], row[2]), max(row[0], row[2])+1):
                coordinateSystem[i][row[1]] = 1
        else:
            print("Unexpected")
            print(row[0], row[2], row[1], row[3])
    allCoordinates.append(coordinateSystem)

x = np.zeros((2, 2))

# sum all coordinates
ventMap = np.zeros((maxVal+1, maxVal+1))
for matrix in allCoordinates:
    ventMap += matrix

total = 0
for row in range(maxVal+1):
    for column in range(maxVal+1):
        if ventMap[row][column] > 1:
            total += 1

print("Total score: ", total)
