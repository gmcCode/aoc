import utils
from time import time
    
def addStones(input):
    stones = set()
    depthAbyss = 0
    for line in input:
        a = [list(map(int, x.split(','))) for x in line.split(" -> ")]
        for i in range(len(a) - 1):
            [x1, y1] = a[i]
            depthAbyss = max(y1, depthAbyss)
            [x2, y2] = a[i + 1]
            depthAbyss = max(y2, depthAbyss)
            if (x1 == x2):
                for j in range (min(y1, y2), max(y1, y2) + 1):
                    stones.add((x1, j))
            if (y1 == y2):
                for j in range (min(x1, x2), max(x1, x2) + 1):
                    stones.add((j, y1))

    return stones, depthAbyss


def part1(input):
    blocked, depth = addStones(input)
    count = 0
    sand = [500, 0]
    while True:
        if sand[1] >= depth:
            break
        elif ((sand[0], sand[1] + 1) not in blocked):
            sand[1] += 1
        elif ((sand[0] - 1, sand[1] + 1) not in blocked):
            sand[0] -= 1
            sand[1] += 1
        elif ((sand[0] + 1, sand[1] + 1) not in blocked):
            sand[0] += 1
            sand[1] += 1
        else: 
            blocked.add(tuple(sand))
            count += 1
            sand = [500, 0]
    print(f"Part 1: {count}")


def part2(input):
    blocked, depth = addStones(input)
    count = 0
    sand = [500, 0]
    while (500,0) not in blocked:
        if sand[1] >= depth + 1:
            blocked.add(tuple(sand))
            count += 1
            sand = [500, 0]
        elif ((sand[0], sand[1] + 1) not in blocked):
            sand[1] += 1
        elif ((sand[0] - 1, sand[1] + 1) not in blocked):
            sand[0] -= 1
            sand[1] += 1
        elif ((sand[0] + 1, sand[1] + 1) not in blocked):
            sand[0] += 1
            sand[1] += 1
        else: 
            blocked.add(tuple(sand))
            count += 1
            sand = [500, 0]
    print(f"Part 2: {count}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)