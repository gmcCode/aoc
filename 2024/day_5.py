from utils import *
from collections import defaultdict


def parseInput(input):
    rules = True
    rulesBook = defaultdict(list)
    rulesBookReverse = defaultdict(list)
    updates = []
    for line in input:
        if len(line) == 0:
            rules = False
            continue

        if rules:
            x, y = line.split("|")
            rulesBook[int(y)].append(int(x))
            rulesBookReverse[int(x)].append(int(y))
        else:
            updates.append(list(map(int, line.split(","))))
    return rulesBook, rulesBookReverse, updates


def checkOrder(rulesBook, update):
    '''Returns True if error occured'''
    errorOccured = False
    possibleErrors = []
    for x in update:
        if not x in possibleErrors:
            possibleErrors += rulesBook[x]
        else:
            return True, x
    return errorOccured, 0


def part1(input):
    result = 0
    rulesBook, _, updates = parseInput(input)
    for update in updates:
        error, _ = checkOrder(rulesBook, update)
        # find middle value
        if not error:
            result += update[int(len(update)/2)]
    return result


def part2(input):
    result = 0
    rulesBook, rulesBookReverse, updates = parseInput(input)
    for update in updates:
        wasBroken = False
        error, x = checkOrder(rulesBook, update)
        if error:
            wasBroken = True
        while error:
            temp = rulesBookReverse[x]
            firstIdx = 0
            for idx, y in enumerate(update):
                if y in temp:
                    firstIdx = idx
                    break
            update.remove(x)
            update.insert(firstIdx, x)
            error, x = checkOrder(rulesBook, update)

        if wasBroken:
            result += update[int(len(update)/2)]

    return result


if __name__ == "__main__":
    input = get_input_as_lines(test=False)

    timed_execution(part1, input)
    timed_execution(part2, input)
