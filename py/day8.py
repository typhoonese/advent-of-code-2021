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

# task 1
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
print("[Task 1]", counter)

# task 2

# segments
# top, middle, bottom
# topLeft, bottomLeft,
# topRight, bottomRight

# 1, 4, 7, 8
# set7 - set1 = top

# from 2,3,5 --> bottom left, top right, bottom right, top left
# set2 - set3 = bottom left
# set2 - set5 = top right + bottom left

# set3 - set2 = bottom right
# set3 - set5 = top right + bottom right

# set5 - set3 = top left
# set5 - set2 = top left

# from 0, 6, 9 --> bottom left, top right, middle
# set0 - set9 = bottom left
# set0 - set6 = top right

# set6 - set0 = middle
# set6 - set9 = bottom left

# set9 - set0 = middle
# set9 - set0 = top right

# others
# set8 - set0 = middle

decodedOutputs = []
for index in range(len(signals)):

    set1 = {}
    set4 = {}
    set7 = {}
    set8 = {}
    setOf6 = []
    setOf5 = []

    for element in signals[index]:
        if len(element) == 2:
            set1 = set(element)
        elif len(element) == 4:
            set4 = set(element)
        elif len(element) == 3:
            set7 = set(element)
        elif len(element) == 7:
            set8 = set(element)
        elif len(element) == 6:
            setOf6.append(set(element))
        elif len(element) == 5:
            setOf5.append(set(element))
        else:
            print("Unexpected")
            break

    # Figure out bottom left, top right, middle
    bL_tR_M = set(())
    bL_tR_M.update(setOf6[0].difference(setOf6[1]))
    bL_tR_M.update(setOf6[0].difference(setOf6[2]))
    bL_tR_M.update(setOf6[1].difference(setOf6[0]))
    bL_tR_M.update(setOf6[1].difference(setOf6[2]))
    bL_tR_M.update(setOf6[2].difference(setOf6[0]))
    bL_tR_M.update(setOf6[2].difference(setOf6[1]))

    # Figure out bottom left, top right, bottom right, top left
    bL_tR_bR_tL = set(())
    bL_tR_bR_tL.update(setOf5[0].difference(setOf5[1]))
    bL_tR_bR_tL.update(setOf5[0].difference(setOf5[2]))
    bL_tR_bR_tL.update(setOf5[1].difference(setOf5[0]))
    bL_tR_bR_tL.update(setOf5[1].difference(setOf5[2]))
    bL_tR_bR_tL.update(setOf5[2].difference(setOf5[0]))
    bL_tR_bR_tL.update(setOf5[2].difference(setOf5[1]))

    # Figure out bottom left, top right
    bL_tR = bL_tR_M.intersection(bL_tR_bR_tL)

    # Figure out top right
    tR = bL_tR.intersection(set1)
    # Figure out bottom left
    bL = bL_tR - tR
    # Figure out bottom right
    bR = set1 - tR
    # Figure out top
    t = set7 - set1
    # Figure out m
    m = bL_tR_M - bL - tR
    # Figure out top left
    tL = bL_tR_bR_tL - bL - tR - bR
    # Figure out bottom
    b = set8 - t - m - bL - bR - tL - tR

    set0 = set(())
    set2 = set(())
    set3 = set(())
    set5 = set(())
    set6 = set(())
    set9 = set(())

    # set0 = t + tL + tR + bL + bR + b
    set0.update(t)
    set0.update(tL)
    set0.update(tR)
    set0.update(bL)
    set0.update(bR)
    set0.update(b)
    # set2 = t + tR + m + bL + b
    set2.update(t)
    set2.update(tR)
    set2.update(m)
    set2.update(bL)
    set2.update(b)
    # set3 = t + tR + m + bR + b
    set3.update(t)
    set3.update(tR)
    set3.update(m)
    set3.update(bR)
    set3.update(b)
    # set5 = t + tL + m + bR + b
    set5.update(t)
    set5.update(tL)
    set5.update(m)
    set5.update(bR)
    set5.update(b)
    # set6 = t + tL + m + bL + bR + b
    set6.update(t)
    set6.update(tL)
    set6.update(m)
    set6.update(bL)
    set6.update(bR)
    set6.update(b)
    # set9 = t + tL + tR + m + bR + b
    set9.update(t)
    set9.update(tL)
    set9.update(tR)
    set9.update(m)
    set9.update(bR)
    set9.update(b)

    encodedOutputs = outputs[index]
    decodedOutput = ''
    for encodedOutput in encodedOutputs:
        encodedSet = set(encodedOutput)
        if encodedSet.issubset(set0) and encodedSet.issuperset(set0):
            decodedOutput += '0'
        elif encodedSet.issubset(set1) and encodedSet.issuperset(set1):
            decodedOutput += '1'
        elif encodedSet.issubset(set2) and encodedSet.issuperset(set2):
            decodedOutput += '2'
        elif encodedSet.issubset(set3) and encodedSet.issuperset(set3):
            decodedOutput += '3'
        elif encodedSet.issubset(set4) and encodedSet.issuperset(set4):
            decodedOutput += '4'
        elif encodedSet.issubset(set5) and encodedSet.issuperset(set5):
            decodedOutput += '5'
        elif encodedSet.issubset(set6) and encodedSet.issuperset(set6):
            decodedOutput += '6'
        elif encodedSet.issubset(set7) and encodedSet.issuperset(set7):
            decodedOutput += '7'
        elif encodedSet.issubset(set8) and encodedSet.issuperset(set8):
            decodedOutput += '8'
        elif encodedSet.issubset(set9) and encodedSet.issuperset(set9):
            decodedOutput += '9'
    decodedOutputs.append(int(decodedOutput))

totalSum = 0
for element in decodedOutputs:
    totalSum += element

print("[Task 2]", totalSum)
