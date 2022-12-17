calCount = []
count = 0
currCals = 0
with open('1in.txt', 'r') as openfileobject:
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


print("\n\nmaxItem: " + str(calCount[len(calCount)-1]))