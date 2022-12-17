calCount = []
count = 0
currCals = 0
with open('C:\\Users\colec\OneDrive\Documents\AdventOfCode22\\1\\1in.txt', 'r') as openfileobject:
    for line in openfileobject:
        if line == '\n':
            calCount.append(currCals);
            currCals = 0
            count += 1
        else:
            currCals += int(line)

calCount.sort()
for x in calCount:
    print(x)

#pt 1
print("\n\nmaxItem: " + str(calCount[len(calCount)-1]))

#pt 2
print('\n\ntop3: ' + str((calCount[len(calCount)-1] + calCount[len(calCount)-2] + calCount[len(calCount)-3])))