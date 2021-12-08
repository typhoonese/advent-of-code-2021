import re

# read file
filePath = '../data/segments.txt'
segmentsFile = open(filePath, 'r')
segmentLines = segmentsFile.readlines()

signals = []
outputs = []
for lineNo in range(len(segmentLines)):
    line = ""
    line = segmentLines[lineNo].split("|")
    signal = line[0].strip().split(" ")
    output = line[1].strip().split(" ")
    signals.append(signal)
    outputs.append(output)

# no of segments
digit1 = 2
digit4 = 4
digit7 = 3
digit8 = 7

counter = 0
for row in outputs:
    for element in row:
        if len(element) == digit1 or len(element) == digit4 or len(element) == digit7 or len(element) == digit8:
            counter += 1
print("[Task 1] Counter: ", counter)
