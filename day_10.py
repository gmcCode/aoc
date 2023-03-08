import utils
from time import time


def part1(input):
    start = time()
    summe = 0
    cycle = 1
    x = 1
    for line in input:
        if "addx" in line:
            cycle += 1
            if (cycle % 40) == 20:
                summe += x * cycle
            x += int(line.split()[1])
        cycle += 1
        if (cycle % 40) == 20:
            summe += x * cycle

    end = time()
    print(f"Part 1: {summe}")
    print(f"Part 1:{end - start}")

def evalScreen(pos, reg):
    if abs(pos - reg) < 2:
        return "#"
    return  "."

def part2(input):
    start = time()   
    screen = ""
    position = 0
    x = 1
    screen += "#"
    for line in input:
        if "addx" in line:
            position += 1
            if (position % 40 == 0):
                position = 0
                screen += "\n"
            screen += evalScreen(position, x)                
            x += int(line.split()[1])
        position += 1
        if (position % 40) == 0:
            position = 0
            screen += "\n"
        screen += evalScreen(position, x)
    end = time()
    print(f"Part 2: \n{screen}")
    print(f"Part 2: {end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
