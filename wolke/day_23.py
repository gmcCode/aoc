import utils
from typing import List, Dict, Tuple
import sys
from time import perf_counter


directions = ["N", "S", "W", "E"]
propo = []
elves = {}

def shuffle_direction():
    global directions
    directions.append(directions.pop(0))

def read_input(input):
    global elves
    elves.clear()
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "#":
                elves[(x, y)] = None

def surroundings_free(coords: Tuple[int, int]) -> bool:
    x, y = coords
    tmp = [ (x, y-1),
            (x+1, y-1),
            (x+1, y),
            (x+1, y+1),
            (x, y+1),
            (x-1, y+1),
            (x-1, y),
            (x-1, y-1)
    ]
    return not any(coord in elves.keys() for coord in tmp)

def next_free_dir(coords: Tuple[int, int]) -> str:
    x, y = coords
    for dir in directions:
        if dir == "N":
            if not any(coord in elves.keys() for coord in [(x, y-1), (x-1, y-1), (x+1, y-1)]):
                return dir
        elif dir == "E":
            if not any(coord in elves.keys() for coord in [(x+1, y+1), (x+1, y), (x+1, y-1)]):
                return dir
        elif dir == "S":
            if not any(coord in elves.keys() for coord in [(x, y+1), (x-1, y+1), (x+1, y+1)]):
                return dir
        elif dir == "W":
            if not any(coord in elves.keys() for coord in [(x-1, y+1), (x-1, y), (x-1, y-1)]):
                return dir

    return None

def propose(coords: Tuple[int, int], dir: str):
    global propo
    x, y = coords
    if dir == "N":
        tmp = (x, y-1)
    elif dir == "E":
        tmp = (x+1, y)
    elif dir == "S":
        tmp = (x, y+1)
    elif dir == "W":
        tmp = (x-1, y)
    propo.append(tmp)
    elves[coords] = tmp

def get_free_ground() -> int:
    min_x = float("inf")
    max_x = 0
    min_y = float("inf")
    max_y = 0

    for elve in elves.keys():
        min_x = min(min_x, elve[0])
        max_x = max(max_x, elve[0])
        min_y = min(min_y, elve[1])
        max_y = max(max_y, elve[1])

    return (max_x - min_x + 1)*(max_y - min_y + 1) - len(elves)

def part1(input: List[str]):
    global elves, propo, directions
    directions = ["N", "S", "W", "E"]

    start = perf_counter()
    read_input(input)

    for round in range(10):
        propo.clear()
        # first half
        for elve in elves.keys():
            if surroundings_free(elve):
                continue
            else:
                dir = next_free_dir(elve)
                if dir != None:
                    propose(elve, dir)
        # second half
        for elve, prop in list(elves.items()):
            if prop == None:
                continue
            else:
                if propo.count(prop) == 1:
                    elves[prop] = None
                    del elves[elve]
                else:
                    elves[elve] = None
        shuffle_direction()

    print(f"Part 1: {get_free_ground()}")
    end = perf_counter()
    print(f"Time: {end - start}")


def part2(input):
    global elves, propo, directions
    directions = ["N", "S", "W", "E"]

    start = perf_counter()
    read_input(input)

    for round in range(sys.maxsize):
        propo.clear()
        someone_moved = False
        # first half
        for elve in elves.keys():
            if surroundings_free(elve):
                continue
            else:
                dir = next_free_dir(elve)
                if dir != None:
                    propose(elve, dir)
        # second half
        for elve, prop in list(elves.items()):
            if prop == None:
                continue
            else:
                if propo.count(prop) == 1:
                    elves[prop] = None
                    del elves[elve]
                    someone_moved = True
                else:
                    elves[elve] = None
        shuffle_direction()
        if not someone_moved:
            print(f"Part 2: {round + 1}")
            break

    end = perf_counter()
    print(f"Time: {end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
