import re


def addPolymer(base):
    addition = polymerRules[base]
    return addition


# read file
filePath = '../data/polymer.txt'
polymerFile = open(filePath, 'r')
polymerRuleLines = polymerFile.readlines()

# create a dictionary of all polymer rules
polymerBase = ''
polymerRules = {}
for line in polymerRuleLines:
    line = (re.sub(" -> ", " ", line)).strip()
    line = line.split(" ")
    if len(line) == 1:
        polymerBase += line[0]
        polymerBase = polymerBase.strip()
    else:
        polymerRules[line[0]] = line[1]

iterationCount = int(
    input("Enter the number of iteration for polymer making:"))
for i in range(iterationCount):
    basePairs = []
    newPolymer = polymerBase[0]
    for j in range(1, len(polymerBase)):
        basePairs.append(polymerBase[j-1] + polymerBase[j])
    for pair in basePairs:
        newPolymer += polymerRules[pair] + pair[1]
    polymerBase = newPolymer

# count the bases of polymer
baseCount = {}

for base in polymerBase:
    if base in baseCount:
        baseCount[base] += 1
    else:
        baseCount[base] = 1

mostUsedBase = max(baseCount, key=baseCount.get)
leastUsedBase = min(baseCount, key=baseCount.get)

print("Most used base  :", mostUsedBase)
print("Least used base :", leastUsedBase)
print("[Task 1] Result :", baseCount[mostUsedBase] - baseCount[leastUsedBase])
