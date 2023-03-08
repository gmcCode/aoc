import utils
from time import time

def move_H(H, dir):
    if dir == "U":
        H[0] += 1
    elif dir == "R":
        H[1] += 1
    elif dir == "D":
        H[0] -= 1
    elif dir == "L":
        H[1] -= 1

def signum(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def move_T(pred, knot):
    if abs(pred[0] - knot[0]) > 1:
        knot[0] += (pred[0] - knot[0]) // 2
        knot[1] += signum(pred[1] - knot[1]) 
    if abs(pred[1] - knot[1]) > 1:
        knot[1] += (pred[1] - knot[1]) // 2
        knot[0] += signum(pred[0] - knot[0]) 


def part1(input):
    start = time()
    knots = [[0, 0] for i in range(2)]
    visited = set()

    for line in input:
        direction, cnt = line.split()
        for _ in range(int(cnt)):
            move_H(knots[0], direction)
            move_T(knots[0], knots[1])
            visited.add(tuple(knots[1]))

    end = time()
    print(f"Part 1: {len(visited)}\t{end - start}")


def part2(input):
    start = time()
    knots = [[0, 0] for i in range(10)]
    visited = set()

    for line in input:
        direction, cnt = line.split()
        for _ in range(int(cnt)):
            move_H(knots[0], direction)
            for i in range(len(knots) - 1):
                move_T(knots[i], knots[i + 1])
            visited.add(tuple(knots[-1]))
    end = time()

    print(f"Part 2: {len(visited)}\t{end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
