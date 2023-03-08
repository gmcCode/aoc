import utils
import re
import math
from time import time

class Monkey:
    ops = { '+': lambda x, y: x + y,
            '*': lambda x, y: x * y}

    def __init__(self, text, lcm=None) -> None:
        self.inspected = 0
        self.lcm = lcm

        operation = text[1].split()
        self.operand = int(operation[-1]) if "old" not in operation[-1] else None
        self.op = self.ops[operation[-2]]

        items = text[0].split(": ")
        self.items = re.split(', ', items[-1])
        self.items = [int(item) for item in self.items]
        self.divide_by = int(text[2].split()[-1])
        self.test_true = int(text[3].split()[-1])
        self.test_false = int(text[4].split()[-1])
    
    def __str__(self) -> str:
        return f"{self.items}"

    def play_round(self):
        self.inspected += len(self.items)

        result = []
        for item in self.items:
            if self.operand == None:
                worry = self.op(item, item)
            else:
                worry = self.op(item, self.operand)
            if self.lcm == None:
                worry = worry // 3
            else:
                worry %= self.lcm

            if worry % self.divide_by == 0:
                result.append((self.test_true, worry))
            else:
                result.append((self.test_false, worry))
        
        self.items.clear()
        return result

def init_monkeys(input, lcm):
    monkeys = []
    for index, line in enumerate(input):
        if "Monkey" in line:
            start = index
        if not line:
            end = index
            monkeys.append(Monkey(input[start + 1:end], lcm))
    monkeys.append(Monkey(input[start + 1::], lcm))

    return monkeys


def part1(input, rounds = 20):
    start = time()
    
    monkeys = init_monkeys(input, None)

    for _ in range(rounds):
        for monkey in monkeys:
            result = monkey.play_round()
            for element in result:
                monkeys[element[0]].items.append(element[1])

    result = []
    for monkey in monkeys:
        result.append(monkey.inspected)
    largest = max(result)
    result.remove(largest)

    result = largest * max(result)

    end = time()
    print(f"Part 1: {result}\t{end - start}")

def part2(input, rounds = 10000):
    start = time()
    
    monkeys = init_monkeys(input, None)
    lcm = math.lcm(*[monkey.divide_by for monkey in monkeys])
    for monkey in monkeys:
        monkey.lcm = lcm

    for _ in range(rounds):
        for monkey in monkeys:
            result = monkey.play_round()
            for element in result:
                monkeys[element[0]].items.append(element[1])

    result = []
    for monkey in monkeys:
        result.append(monkey.inspected)
    largest = max(result)
    result.remove(largest)

    result = largest * max(result)

    end = time()
    print(f"Part 2: {result}\t{end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
