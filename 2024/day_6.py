from utils import *
from collections import defaultdict

def parse_input(input):
    map_size_y = len(input)
    map_size_x = len(input[0])
    start_pos = []
    obstacles = [defaultdict(list), defaultdict(list)]
    for i, y in enumerate(input):
        for j, x in enumerate(y):
            if x == "#":
                obstacles[0][i] += [j]
                obstacles[1][j] += [i]
            elif x == "^":
                start_pos = (j, i)
    return map_size_x, map_size_y, start_pos, obstacles

visited = set()

def part1(input):
    map_size_x, map_size_y, start_pos, obstacles = parse_input(input)
    curr_pos = list(start_pos)
    visited.add(start_pos)
    on_y_axis = 1
    facing_negative = 1
    while True:
        if facing_negative:
            next_point = -1
            for x in obstacles[on_y_axis][curr_pos[abs(on_y_axis-1)]]:
                if next_point < x < curr_pos[on_y_axis]:
                    next_point = x
            temp = curr_pos[on_y_axis] - 1
            if on_y_axis:
                while temp > next_point:
                    visited.add((curr_pos[0], temp))
                    temp -= 1
                facing_negative = 0
            else:
                while temp > next_point:
                    visited.add((temp, curr_pos[1]))
                    temp -= 1
            if next_point == -1:
                break
            curr_pos[on_y_axis] = next_point + 1
            on_y_axis = abs(on_y_axis-1)
        else:
            if on_y_axis:
                next_point = map_size_y
            else:
                next_point = map_size_x
            for x in obstacles[on_y_axis][curr_pos[abs(on_y_axis-1)]]:
                if next_point > x > curr_pos[on_y_axis]:
                    next_point = x
            temp = curr_pos[on_y_axis] + 1
            if on_y_axis:
                while temp < next_point:
                    visited.add((curr_pos[0], temp))
                    temp += 1
                facing_negative = 1
            else:
                while temp < next_point:
                    visited.add((temp, curr_pos[1]))
                    temp += 1
            if on_y_axis and next_point == map_size_y or (not on_y_axis and (next_point == map_size_x)):
                break
            curr_pos[on_y_axis] = next_point - 1
            on_y_axis = abs(on_y_axis-1)

    return len(visited)


def checkLoop(map_size_x, map_size_y, curr_pos, obstacles):
    visited = set()
    on_y_axis = 1
    facing_negative = 1
    while True:
        last_pos = tuple(curr_pos)
        if facing_negative:
            next_point = -1
            for x in obstacles[on_y_axis][curr_pos[abs(on_y_axis-1)]]:
                if next_point < x < curr_pos[on_y_axis]:
                    next_point = x
            if next_point == -1:
                return False
            curr_pos[on_y_axis] = next_point + 1
            if tuple(curr_pos) in visited and not tuple(curr_pos) == last_pos:
                return True
            else:
                visited.add(tuple(curr_pos))
            facing_negative -= on_y_axis
            on_y_axis = abs(on_y_axis-1)
        else:
            if on_y_axis:
                next_point = map_size_y
            else:
                next_point = map_size_x
            for x in obstacles[on_y_axis][curr_pos[abs(on_y_axis-1)]]:
                if next_point > x > curr_pos[on_y_axis]:
                    next_point = x
            if (on_y_axis and next_point == map_size_y) or (not on_y_axis and next_point == map_size_x):
                return False
            curr_pos[on_y_axis] = next_point - 1
            if tuple(curr_pos) in visited and not tuple(curr_pos) == last_pos:
                return True
            else:
                visited.add(tuple(curr_pos))
            facing_negative += on_y_axis
            on_y_axis = abs(on_y_axis-1)


def part2(input):
    map_size_x, map_size_y, start_pos, obstacles = parse_input(input)
    result = 0
    for x in visited:
        curr_pos = list(start_pos)
        if x == tuple(curr_pos):
            continue
        obstacles[0][x[1]] += [x[0]]
        obstacles[1][x[0]] += [x[1]]
        if checkLoop(map_size_x, map_size_y, curr_pos, obstacles):
            result += 1
        obstacles[0][x[1]].remove(x[0])
        obstacles[1][x[0]].remove(x[1])
    return result



if __name__ == "__main__":
    input = get_input_as_lines(test=True)

    timed_execution(part1, input)
    timed_execution(part2, input)
