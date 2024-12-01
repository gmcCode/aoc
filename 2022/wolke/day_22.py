import utils
from time import time


def stuff_list(a, elem):
    result = [elem] * (len(a) * 2 - 1)
    result[0::2] = a
    return result


def parse_input(input):
    end_map = input.index("")
    row_map, col_map = [], []
    walls = set()
    for i, line in enumerate(input[0:end_map]):
        if "#" in line:
            tmp = line.index("#")
        else:
            tmp = len(line)
        row_map.append((min(line.index("."), tmp), len(line) - 1))
        for j, x in enumerate(line):
            if x == "#":
                walls.add((j, i))
    number_of_cols = max(x[1] for x in row_map)
    for i in range(number_of_cols):
        j = 0
        while i < row_map[j][0] or i > row_map[j][1]:
            j += 1
        tmp = j
        while j+1 < end_map and not (i < row_map[j+1][0] or i > row_map[j+1][1]):
            j += 1
        col_map.append((tmp, j))

    walk = input[end_map + 1]
    walk = stuff_list(walk.split('R'), 'R')
    walk = [stuff_list(x.split('L'), 'L') for x in walk]
    walk = [item for sublist in walk for item in sublist]
    print(row_map[0])
    return row_map, col_map, walls, walk


def part1(input):
    row_map, col_map, walls, walk = parse_input(input) #flat_list = [item for sublist in l for item in sublist]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    current_pos = (row_map[0][0], 0)
    print(current_pos)
    turn = 0
    for step in walk:
        if step == 'R':
            turn = (turn + 1) % 4
        elif step == 'L':
            turn = (turn - 1) % 4
        else:
            step = int(step)
            for i in range(step):
                tmp = current_pos
                if turn == 0 and current_pos[0] + 1 > row_map[current_pos[1]][1]:
                    tmp = (row_map[current_pos[1]][0], current_pos[1])
                elif turn == 1 and current_pos[1] + 1 > col_map[current_pos[0]][1]:
                    tmp = (current_pos[0], col_map[current_pos[0]][0])
                elif turn == 2 and current_pos[0] - 1 < row_map[current_pos[1]][0]:
                    tmp = (row_map[current_pos[1]][1], current_pos[1])
                elif turn == 3 and current_pos[1] - 1 < col_map[current_pos[0]][0]:
                    tmp = (current_pos[0], col_map[current_pos[0]][1])
                else:
                    tmp = tuple(sum(x) for x in zip(current_pos, directions[turn]))

                if tmp in walls:
                    break
                current_pos = tmp
            #print(current_pos, turn)
    print((current_pos[1] + 1) * 1000 + (current_pos[0] + 1) * 4 + turn)
    return None


def part2(input):
    #hier fehlt einfach eine derbe hohle Unterscheidung von 15 Fällen
    pass


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    start = time()
    part1(input)
    end = time()
    print(f"Laufzeit Part 1: {end - start}")

    start = time()
    part2(input)
    end = time()
    print(f"Laufzeit Part 2: {end - start}")
