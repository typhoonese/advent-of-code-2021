import copy

# read file
filePath = '../data/lanternFish.txt'
lanternFishTimerFile = open(filePath, 'r')
lanternFishTimerLines = lanternFishTimerFile.readlines()

currentLanternFish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in lanternFishTimerLines:
    line = line.strip().split(",")
    line = [int(i) for i in line]
    for timer in line:
        currentLanternFish[timer] += 1

day = int(input("Enter the duration of lantern fish simulation (in days): "))

for dayNo in range(day):
    newDay = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index in range(len(currentLanternFish)):
        newDay[0] = currentLanternFish[1]
        newDay[1] = currentLanternFish[2]
        newDay[2] = currentLanternFish[3]
        newDay[3] = currentLanternFish[4]
        newDay[4] = currentLanternFish[5]
        newDay[5] = currentLanternFish[6]
        newDay[6] = currentLanternFish[7] + currentLanternFish[0]
        newDay[7] = currentLanternFish[8]
        newDay[8] = currentLanternFish[0]

    currentLanternFish = newDay

totalLanternFish = 0
for element in currentLanternFish:
    totalLanternFish += element

print("At the end of the simulation, the number of lantern fish will be",
      totalLanternFish)
