from utils import *


def part1(input):

    sum = 0
    for line in input:
        zeile = line.split()
        bigger = None
        geht = None
        for i in range(0, len(zeile)-1):
            diff = int(zeile[i]) - int(zeile[i+1])
            if diff >= -3 and diff <= -1 and (bigger == None or bigger == True):
                geht = True
                bigger = True
            elif diff <= 3 and diff >= 1 and (bigger == None or bigger == False):
                geht = True
                bigger = False
            else:
                geht = False
                break
        if geht == True:
            sum += 1

    return sum


def partZwoQuickAndDirty(input):

    sum = 0

    def denkdirwasaus(zeile):
        bigger = None
        summe = 0
        geht = None
        badde = 0
        for i in range(0, len(zeile)-1):
            diff = int(zeile[i]) - int(zeile[i+1])
            if diff >= -3 and diff <= -1 and (bigger == None or bigger == True):
                geht = True
                bigger = True
            elif diff <= 3 and diff >= 1 and (bigger == None or bigger == False):
                geht = True
                bigger = False
            else:
                geht = False
                zeile.pop(i+1)
                badde += 1
                break

        if geht == True:
            summe += 1

        return summe, badde, zeile

    for line in input:
        zeile = line.split()  # x [(sum), (bad), zeile]
        bad = 0
        sum = 0
        x = [0, 0, []]
        while x[1] == 0 and x[0] == 0:
            x = denkdirwasaus(zeile)
            if x[1] == 0:
                sum += 1
            elif x[1] == 1:
                x = denkdirwasaus(x[2])

    return sum

# (1, 0, ['7', '6', '4', '2', '1'])
# (0, 1, ['1', '2', '8', '9'])
# (0, 1, ['9', '7', '6', '1'])
# (0, 1, ['1', '3', '4', '5'])
# (0, 1, ['8', '6', '4', '1'])
# (1, 0, ['1', '3', '6', '7', '9'])


def partfancy(input):
    list1 = list(map(lambda line: list(map(int, line.split())), input))
    list2 = list(map(lambda line: [x-y
                 for x, y in zip(line, line[1:])], list1))
    list3 = list(map(lambda z: all(i >= 1 and i <= 3 for i in z)
                 or all(i <= -1 and i >= -3 for i in z), list2))
    return sum(list(map(int, list3)))


def checkList(list):
    temp = [x-y for x, y in zip(list, list[1:])]
    if all(i >= 1 and i <= 3 for i in temp) or all(i <= -1 and i >= -3 for i in temp):
        return True
    return False


def part2(input):
    sum = 0
    list1 = list(map(lambda line: list(map(int, line.split())), input))
    for line in list1:
        if checkList(line):
            sum += 1
        else:
            for idx, _ in enumerate(line):
                temp = line.pop(idx)
                if checkList(line):
                    sum += 1
                    break
                line.insert(idx, temp)

    return sum


if __name__ == "__main__":
    input = get_input_as_lines(test=False)

    timed_execution(part1, input)
    timed_execution(partfancy, input)
    timed_execution(part2, input)
    timed_execution(partZwoQuickAndDirty, input)
