import statistics

# read file
filePath = '../data/crabMarines.txt'
crabMarinePositionFile = open(filePath, 'r')
crabMarinePositionLines = crabMarinePositionFile.readlines()

# create a list of horizontal positions
positions = []
for line in crabMarinePositionLines:
    line = line.strip().split(",")
    line = [int(i) for i in line]
    for position in line:
        positions.append((position))

# part 1

# calculate median
median = statistics.median(positions)
print("median:", median)

fuelCostMedian = 0
for position in positions:
    fuelCostMedian += abs(position-median)

print("[Part 1] Fuel cost by median", fuelCostMedian)

# part 2

# calculate mean
# TODO: doesn't work needs investigation
mean = round(statistics.mean(positions))
print("mean:", mean)

fuelCostMean = 0
for position in positions:
    if (position != mean):
        numOfSteps = abs(position-mean)
        if numOfSteps == 1:
            fuelCostMean += 1
        else:
            fuelCostMean += (numOfSteps+1)*numOfSteps / 2

print("[Part 2] Fuel cost by mean", fuelCostMean)

# calculate by brute force
minCost = None
position = None
for i in range(max(positions)+1):
    fuelCostBrute = 0
    for position in positions:
        if (position != i):
            numOfSteps = abs(position-i)
            if numOfSteps == 1:
                fuelCostBrute += 1
            else:
                fuelCostBrute += (numOfSteps+1)*numOfSteps / 2
    if (minCost == None or minCost > fuelCostBrute):
        minCost = fuelCostBrute
        position = i
print("Min fuel cost via brute force", minCost, position)
