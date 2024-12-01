import utils
from typing import List
from time import perf_counter


class Number:
    def __init__(self, value, before) -> None:
        self.value = value
        self.before = before
        self.after = None

    def __repr__(self) -> str:
        return str(self.value)


def readInput(input, use_key = False):
    numbers = []
    key = 811589153
    last = None
    for line in input:
        if use_key:
            val = int(line) * key
        else:
            val = int(line)
        numbers.append(Number(val, last))
        last = numbers[-1]
    numbers[0].before = numbers[-1]

    for id, nr in enumerate(numbers[0:-1]):
        nr.after = numbers[id + 1]

    numbers[-1].after = numbers[0]
    return numbers


def searchNode(numbers: List[Number], nr: Number, value: int, max_steps: int):
    next = nr
    if value > 0:
        for i in range(value % max_steps):
            next = next.after
        return (next, next.after)
    elif value < 0:
        for i in range(abs(value) % max_steps):
            next = next.before
        return (next.before, next)


def calcFinish(numbers):
    max_steps = len(numbers) - 1
    for nr in numbers:
        value = nr.value
        if value != 0:
            nodes = searchNode(numbers, nr, value, max_steps)
            # if value > 0 and nodes[0] == nr:
            #     continue
            # elif value < 0 and nodes[1] == nr:
            #     continue
            nodes[0].after = nr
            nodes[1].before = nr
            nr.before.after = nr.after
            nr.after.before = nr.before
            nr.before = nodes[0]
            nr.after = nodes[1]

def print_list(numbers):
    result = "["
    current = numbers[0]
    for _ in range(len(numbers)):
        result += f"{str(current.value)} " 
        current = current.after
    print(f"{result}]")

def part1(input):
    start = perf_counter()
    summe = 0

    numbers = readInput(input)
    calcFinish(numbers)

    ids = [1000, 2000, 3000]
    node = numbers[0]
    while node.value != 0:
        node = node.after
    
    for id in ids:
        first = node
        # rest = id % len(numbers)
        for _ in range(id):
            first = first.after
        summe += first.value
    
    print(f'Part 1: {summe}')
    end = perf_counter()
    print(f"Time: {end - start}")


def part2(input):
    start = perf_counter()
    summe = 0

    numbers = readInput(input, True)
    for _ in range(10):
        calcFinish(numbers)

    ids = [1000, 2000, 3000]
    node = numbers[0]
    while node.value != 0:
        node = node.after
    
    for id in ids:
        first = node
        # rest = id % len(numbers)
        for _ in range(id):
            first = first.after
        summe += first.value
    
    print(f'Part 2: {summe}')
    end = perf_counter()
    print(f"Time: {end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    # part1(input)
    part2(input)
