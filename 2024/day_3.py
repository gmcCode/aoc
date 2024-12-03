from utils import *
import re


def part1Regex(input):
    sum = 0
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    for line in input:
        matches = pattern.findall(line)

        for match in matches:
            sum += int(match[0]) * int(match[1])
    return sum


def part2Regex(input):
    result = 0
    active = True
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")

    for line in input:
        matches = pattern.findall(line)

        for match in matches:
            if match[3] == "don't()":
                active = False
            elif match[2] == "do()":
                active = True
            elif active:
                result += int(match[0]) * int(match[1])
    return result


def part1(input):
    sum = 0

    for line in input:
        multiplications = []
        numericelements = []
        noe = line.split("mul(")
        for i in range(len(noe)):
            multiplications += noe[i].split(")")
        for element in multiplications:
            numericelements.append(element.split(','))
        for i in range(0, len(numericelements), 1):
            if len(numericelements[i]) == 2:
                a = numericelements[i][0].isnumeric()
                b = numericelements[i][1].isnumeric()  # [[x,y], [zhsdfgjh]]
                x = numericelements[i][0]
                y = numericelements[i][1]
                if a == True and b == True and int(x) < 1000 and int(y) < 1000:
                    sum += int(x)*int(y)
    return sum


def part2(input):
    summe = 0

    line = "".join(input)

    multiplications = []
    numericelements = []

    temp = line.split("do()")
    a = [x.split("don't()")[0] for x in temp]
    a = "".join(a)

    noe = a.split("mul(")
    for i in range(len(noe)):
        multiplications += noe[i].split(")")
    for element in multiplications:
        numericelements.append(element.split(','))
    for i in range(0, len(numericelements), 1):
        if len(numericelements[i]) == 2:
            a = numericelements[i][0].isnumeric()
            b = numericelements[i][1].isnumeric()  # [[x,y], [zhsdfgjh]]
            x = numericelements[i][0]
            y = numericelements[i][1]
            if a == True and b == True and int(x) < 1000 and int(y) < 1000:
                summe += int(x)*int(y)
    return summe


if __name__ == "__main__":
    input = get_input_as_lines(test=False)

    timed_execution(part1Regex, input)
    timed_execution(part2Regex, input)
    timed_execution(part1, input)
    timed_execution(part2, input)
