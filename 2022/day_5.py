import utils

def getCranes(input): #gets number of Stacks and the maximal height
    lineCount = 0
    while(len(input[lineCount])) != 0:
        lineCount+=1
    NumberCranes = (input[lineCount-1][len(input[lineCount-1])-1])
    return int(NumberCranes) , lineCount - 1

def getStacks(input,NumberStacks, lineCount):   #liest die Stacks ein
    Cranes = [[] for _ in range(NumberStacks)]

    for i in range(lineCount - 1, -1, -1):      #geht jede Spalte durch
        for j in range(1, len(input[i]), 4):             
            if input[i][j] != ' ':              #testet ob Crane vorhanden ist in der Zeile
                Cranes[j//4].append(input[i][j])
    return Cranes

def getMoves(input) -> list:                    #liest Züge ein
    Moves = []
    for line in input:
        s = line.split()
        Moves.append([int(s[1]), int(s[3]) - 1, int(s[5]) - 1])
    return Moves

def doMove(stacks, m) -> list:
    for i in range (0, m[0]):
        stacks[m[2]] += stacks[m[1]].pop()
    return stacks

def doMoveWithSameOrder(stacks, m) -> list:
    helpList = []
    for i in range (0, m[0]):
        helpList += stacks[m[1]].pop()  
    for i in range (0, m[0]):
        stacks[m[2]] += helpList.pop()  
    
    return stacks


def part1(input):
    NumberCranes , lineCount = getCranes(input)
    stacks = getStacks(input,NumberCranes, lineCount)
    moves = getMoves(input[lineCount+2:])
    for move in moves:
        stacks = doMove(stacks, move)
    ausgabe = ''
    for s in stacks:
        ausgabe += s[-1]
    print(f"Part 1: {ausgabe}")

def part2(input):
    NumberCranes , lineCount = getCranes(input)
    stacks = getStacks(input,NumberCranes, lineCount)
    moves = getMoves(input[lineCount+2:])
    for move in moves:
        stacks = doMoveWithSameOrder(stacks, move)
    ausgabe = ''
    for s in stacks:
        ausgabe += s[-1]
    print(f"Part 2: {ausgabe}")

if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)