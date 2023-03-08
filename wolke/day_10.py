import utils
from time import time

result = 0
check_cycles = [20, 60, 100, 140, 180, 220]

def check_cycle(tick, X):
    global result
    if tick in check_cycles:
        result += tick * X

def part1(input):
    start = time()
    tick = 0
    X = 1

    for line in input:
        if "noop" in line:
            tick += 1
            check_cycle(tick, X)
        elif "addx" in line:
            tick += 1
            check_cycle(tick, X)
            tick += 1
            check_cycle(tick, X)
            X += int(line.split()[1])

    end = time()
    print(f"Part 1: {result}\t{end - start}")


def print_crt(crt):
    for line in crt:
        print("".join(line))


def draw_crt(tick, X, crt):
    sprite = X % 40
    x = tick % 40
    Y = int(tick / 40)
    if x in [sprite - 1, sprite, sprite + 1]:
        crt[Y][x] = "█"


def part2(input):
    start = time()
    tick = 0
    X = 1
    crt = [["░"] * 40 for _ in range(6)]

    for line in input:
        if "noop" in line:
            draw_crt(tick, X, crt)
            tick += 1
        elif "addx" in line:
            draw_crt(tick, X, crt)
            tick += 1
            draw_crt(tick, X, crt)
            tick += 1
            X += int(line.split()[1])
    
    end = time()
    print_crt(crt)
    print(f"Part 2: \t{end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
