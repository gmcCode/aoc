import utils
import re
from time import time


class Game:
    def __init__(self, input) -> None:
        self.input = input
        self.iter = iter(input)
        self.current_stone = 0
        self.input_count = 0

    def next_input(self):
        try:
            self.input_count += 1
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.input)
            self.input_count = 0
            return next(self.iter)

    def next_stone(self, y):
        if self.current_stone == 0:
            self.current_stone += 1
            return self.Stone(0, y, 3, 1)
        elif self.current_stone == 1:
            self.current_stone += 1
            return self.Stone(1, y, 2, 3)
        elif self.current_stone == 2:
            self.current_stone += 1
            return self.Stone(2, y, 2, 3)
        elif self.current_stone == 3:
            self.current_stone += 1
            return self.Stone(3, y, 0, 4)
        elif self.current_stone == 4:
            self.current_stone = 0
            return self.Stone(4, y, 1, 2)

    class Stone:
        def __init__(self, type, down, width, height) -> None:
            self.type = type
            self.left = 2
            self.down = down
            self.width = width
            self.height = height

        def coords(self):
            if self.type == 0:
                return [
                    (self.left, self.down),
                    (self.left + 1, self.down),
                    (self.left + 2, self.down),
                    (self.left + 3, self.down),
                ]
            elif self.type == 1:
                return [
                    (self.left, self.down + 1),
                    (self.left + 1, self.down + 1),
                    (self.left + 1, self.down + 2),
                    (self.left + 1, self.down),
                    (self.left + 2, self.down + 1),
                ]
            elif self.type == 2:
                return [
                    (self.left    , self.down),
                    (self.left + 1, self.down),
                    (self.left + 2, self.down),
                    (self.left + 2, self.down + 1),
                    (self.left + 2, self.down + 2),
                ]
            elif self.type == 3:
                return [
                    (self.left, self.down),
                    (self.left, self.down + 1),
                    (self.left, self.down + 2),
                    (self.left, self.down + 3),
                ]
            elif self.type == 4:
                return [
                    (self.left    , self.down),
                    (self.left + 1, self.down + 1),
                    (self.left    , self.down + 1),
                    (self.left + 1, self.down),
                ]


def part1(input):
    start = time()

    g = Game(input[0])

    seen_states = set()
    top = 0
    occupied_fields = set(
        [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)]
    )
    stone_cnt = 0
    while stone_cnt < 1000000:
        stone = g.next_stone(top + 3)
        while True:
            input = g.next_input()
            if input == "<" and stone.left >= 1:
                # links
                allowed = True
                for coord in stone.coords():
                    if (coord[0] - 1, coord[1]) in occupied_fields:
                        allowed = False
                if allowed:
                    stone.left -= 1
            elif input == ">" and stone.left + stone.width <= 5:
                # rechts
                allowed = True
                for coord in stone.coords():
                    if (coord[0] + 1, coord[1]) in occupied_fields:
                        allowed = False
                if allowed:
                    stone.left += 1

            # runter
            allowed = True
            for coord in stone.coords():
                if (coord[0], coord[1] - 1) in occupied_fields:
                    allowed = False
            if allowed:
                stone.down -= 1
            else:
                break
        stone_cnt += 1
        occupied_fields.update(stone.coords())
        top = max(top, stone.down + stone.height)
        seen_states(hash((stone.type, )))

    print(f"Part 1: {top}")
    end = time()
    print(f"Time: {end - start}")


def part2(input):
    start = time()
    tart = time()

    g = Game(input[0])

    seen_states = {}
    top = 0
    h_map = [0 for i in range(7)]
    occupied_fields = set(
        [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)]
    )
    stone_cnt = 0
    skipped = False
    bound = 1000000000000
    while stone_cnt < bound:
        stone = g.next_stone(top + 3)
        while True:
            input = g.next_input()
            if input == "<" and stone.left >= 1:
                # links
                allowed = True
                for coord in stone.coords():
                    if (coord[0] - 1, coord[1]) in occupied_fields:
                        allowed = False
                if allowed:
                    stone.left -= 1
            elif input == ">" and stone.left + stone.width <= 5:
                # rechts
                allowed = True
                for coord in stone.coords():
                    if (coord[0] + 1, coord[1]) in occupied_fields:
                        allowed = False
                if allowed:
                    stone.left += 1

            # runter
            allowed = True
            for coord in stone.coords():
                if (coord[0], coord[1] - 1) in occupied_fields:
                    allowed = False
            if allowed:
                stone.down -= 1
            else:
                break
        stone_cnt += 1
        occupied_fields.update(stone.coords())
        top = max(top, stone.down + stone.height)

        if not skipped:
            for coord in stone.coords():
                h_map[coord[0]] = max(h_map[coord[0]], coord[1])
            tmp = (stone.type, g.input_count, tuple([top - y for y in h_map]), 0)
            if tmp not in seen_states.keys():
                seen_states[tmp] = (top, stone_cnt)
            elif tmp in seen_states.keys():
                tmp = (stone.type, g.input_count, tuple([top - y for y in h_map]), 1)
                if tmp not in seen_states.keys():
                    seen_states[tmp] = (top, stone_cnt)
                else: 
                    old_top, old_stone_cnt = seen_states[tmp]
                    diff_top = top - old_top
                    diff_stone_cnt = stone_cnt - old_stone_cnt
                    mult = bound//diff_stone_cnt - 2
                    stone_cnt += mult * diff_stone_cnt
                    #top += mult * diff_top
                    skipped = True
                    print(stone_cnt)
                
    print(f"Part 2: {top + mult * diff_top}")
    end = time()
    print(f"Time: {end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    # part1(input)
    part2(input)
