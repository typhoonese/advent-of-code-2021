import numpy as np


def findNeighbors(position):
    neighbors = []
    (maxX, maxY) = arrangement.shape
    (minX, minY) = (0, 0)
    # left top diagonal
    if position[0]-1 >= minX and position[1]-1 >= minY:
        neighbors.append((position[0]-1, position[1]-1))
    # right bottom diagonal
    if position[0]+1 < maxX and position[1]+1 < maxY:
        neighbors.append((position[0]+1, position[1]+1))
    # right
    if position[1]+1 < maxY:
        neighbors.append((position[0], position[1]+1))
    # left
    if position[1]-1 >= minY:
        neighbors.append((position[0], position[1]-1))
     # bottom
    if position[0]+1 < maxX:
        neighbors.append((position[0]+1, position[1]))
    # top
    if position[0]-1 >= minX:
        neighbors.append((position[0]-1, position[1]))
    # left bottom diagonal
    if position[0]+1 < maxX and position[1]-1 >= minY:
        neighbors.append((position[0]+1, position[1]-1))
    # right top diagonal
    if position[0]-1 >= minX and position[1]+1 < maxY:
        neighbors.append((position[0]-1, position[1]+1))

    return neighbors


def checkFlash(position, flashed):
    row = position[0]
    column = position[1]
    # increase each energy level by 1 every time
    if (row, column) not in flashed:
        arrangement[row][column] += 1
        if (arrangement[row][column] > flashThreshhold):
            # it will flash and energy will be resetted to 0
            arrangement[row][column] = 0
            flashed.append((row, column))
            neighbors = findNeighbors((row, column))
            for neighbor in neighbors:
                flashed = checkFlash(neighbor, flashed)
    return flashed


def iterateStep(arrangement, flashed):
    (maxX, maxY) = arrangement.shape
    for row in range(maxX):
        for column in range(maxY):
            flashed = checkFlash((row, column), flashed)
    # print("Step: {0}, total count of flash: {1}".format(i, len(flashed)))
    return flashed


# read file
filePath = '../data/dumboOctopus.txt'
arrangementFile = open(filePath, 'r')
arrangementLines = arrangementFile.readlines()

arrangementMain = np.zeros((10, 10))

for row in range(10):
    for column in range(10):
        arrangementMain[row][column] = int(arrangementLines[row][column])
# make a copy for task 1 and task 2
arrangement = arrangementMain.copy()
# threshold of when they might flash
flashThreshhold = 9

# Task 1
numberOfStep = int(input('Enter number of steps for Task 1:'))
totalFlashCount = 0
for i in range(numberOfStep):
    flashed = []
    flashed = iterateStep(arrangement, flashed)
    totalFlashCount += len(flashed)

print("[Task 1]: Total flash count:", totalFlashCount)

# Task 2
step = 0
flashCount = 0
arrangement = arrangementMain.copy()
while (flashCount != 100):
    step += 1
    flashed = []
    flashed = iterateStep(arrangement, flashed)
    flashCount = len(flashed)

print("[Task 2]: At step {0}, all will flash at the same time".format(step))
