score = 0
playerMove = []
oppMove = []

scoreDict = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3 # scissor
}
with open('C:\\Users\colec\OneDrive\Documents\AdventOfCode22\\2\in.txt', 'r') as openfileobject:
    for i, line in enumerate(openfileobject):
        oppMove.append(line[0])
        playerMove.append(line[2]) 

    for i, playerMove in enumerate(playerMove):
        if (oppMove[i] == 'A'):
            if (playerMove == "X"):
                score += 3
            elif (playerMove == "Y"):
                score += 6
        elif (oppMove[i] == 'B'):
            if (playerMove == "Y"):
                score += 3
            if (playerMove == "Z"):
                score += 6
        elif (oppMove[i] == 'C'):
            if (playerMove == "Z"):
                score += 3
            elif (playerMove == "X"):
                score += 6
        score += scoreDict[playerMove]    

#pt 1
print("score: " + str(score))

#pt 2


