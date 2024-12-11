from utils import *

from collections import defaultdict


class Stone:
    def __init__(self, number, next=None):
        self.next = next
        self.number = number

    def split(self):
        string_number = str(self.number)
        new_number = int(string_number[len(string_number) // 2:])
        self.number = int(string_number[:len(string_number) // 2])
        new_stone = Stone(next=self.next, number=new_number)
        self.next = new_stone


class StoneHandler:
    def __init__(self):
        self.root = None

    def appendNewStone(self, number):
        new_stone = Stone(number)
        if not self.root:
            self.root = new_stone
            return

        current_stone = self.root
        while current_stone.next:
            current_stone = current_stone.next
        current_stone.next = new_stone

    def __iter__(self):
        self.current = self.root
        return self

    def __next__(self):
        if self.current:
            current_temp = self.current
            self.current = self.current.next
            return current_temp
        else:
            raise StopIteration


def part1(input):
    result = 0
    list = StoneHandler()
    max_iterations = 25

    for number in input[0].split():
        list.appendNewStone(int(number))

    for _ in range(max_iterations):
        for stone in list:
            if stone.number == 0:
                stone.number = 1
            elif len(str(stone.number)) % 2 == 0:
                stone.split()
            else:
                stone.number *= 2024

    for stone in list:
        result += 1

    return result


class CustomDefaultDict(defaultdict):
    def __missing__(self, key):
        value = self.default_factory(key)
        self[key] = value
        return value


def pre_calc(number):
    stones = [number]
    for _ in range(3):
        new_stones = []
        for stone in stones:
            str_stone = str(stone)
            if stone == 0:
                new_stones += [1]
            elif len(str_stone) % 2 == 0:
                new_stones += [int(str_stone[len(str_stone) // 2:]),
                               int(str_stone[:len(str_stone) // 2])]
            else:
                new_stones += [stone * 2024]
        stones = new_stones.copy()

    result = [(x, stones.count(x)) for x in set(stones)]

    return result


def part2(input):
    result = 0
    max_iterations = 75 // 3  # <-- This number is scientifically proven !!!

    start_stones = list(map(int, input[0].split()))
    curr_stones = defaultdict(int)
    for stone in start_stones:
        curr_stones[stone] += 1

    curr_next_stones = defaultdict(int)
    pre_calculated = CustomDefaultDict(pre_calc)

    for _ in range(max_iterations):
        for stone in curr_stones.keys():
            factor = curr_stones[stone]
            for a, b in pre_calculated[stone]:
                curr_next_stones[a] += factor * b

        curr_stones = curr_next_stones.copy()
        curr_next_stones.clear()

    for x in curr_stones.values():
        result += x
    return result


if __name__ == "__main__":
    input = get_input_as_lines(test=False)

    timed_execution(part1, input, number=10)
    timed_execution(part2, input, number=10)
