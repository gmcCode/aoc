from utils import *

mapsize_x = 0
mapsize_y = 0


def on_map(x, y):
    if 0 <= x < mapsize_x and 0 <= y < mapsize_y:
        return True
    return False


def part1(input):
    global mapsize_x, mapsize_y
    result = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    terrain = []
    mapsize_x = len(input[0])
    mapsize_y = len(input)
    # Karte die an jeder Stelle 0 hat
    poss_ways_terrain = [
        [set() for _ in range(mapsize_x)] for _ in range(mapsize_y)]
    for line in input:
        terrain.append(list(map(int, list(line))))
    counter = 8
    for x in range(mapsize_x):
        for y in range(mapsize_y):
            if terrain[y][x] == 9:
                poss_ways_terrain[y][x].add((x, y))
    while counter >= 0:
        for x in range(mapsize_x):
            for y in range(mapsize_y):
                if terrain[y][x] == counter:
                    for (dx, dy) in directions:
                        nx, ny = x+dx, y+dy
                        if on_map(nx, ny) and terrain[ny][nx] == counter + 1:
                            poss_ways_terrain[y][x].update(
                                poss_ways_terrain[ny][nx])
                    if counter == 0:
                        result += len(poss_ways_terrain[y][x])
        counter -= 1
    return result


def part2(input):
    global mapsize_x, mapsize_y
    result = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    terrain = []
    mapsize_x = len(input[0])
    mapsize_y = len(input)
    # Karte die an jeder Stelle 0 hat
    poss_ways_terrain = [
        [0 for _ in range(mapsize_x)] for _ in range(mapsize_y)]
    for line in input:
        terrain.append(list(map(int, list(line))))
    counter = 8
    for x in range(mapsize_x):
        for y in range(mapsize_y):
            if terrain[y][x] == 9:
                poss_ways_terrain[y][x] = 1
    while counter >= 0:
        for x in range(mapsize_x):
            for y in range(mapsize_y):
                if terrain[y][x] == counter:
                    for (dx, dy) in directions:
                        nx, ny = x+dx, y+dy
                        if on_map(nx, ny) and terrain[ny][nx] == counter + 1:
                            poss_ways_terrain[y][x] += poss_ways_terrain[ny][nx]
                    if counter == 0:
                        result += poss_ways_terrain[y][x]
        counter -= 1
    return result


if __name__ == "__main__":
    input = get_input_as_lines(test=False)

    timed_execution(part1, input, number=10)
    timed_execution(part2, input, number=10)
