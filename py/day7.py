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

# calculate median
median = statistics.median(positions)

fuelCostMedian = 0
for position in positions:
    fuelCostMedian += abs(position-median)

print("Fuel cost  median", fuelCostMedian)
