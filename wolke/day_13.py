import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import utils
from time import time

class Packet:
    def __init__(self, value) -> None:
        self.value = value

    def __lt__(self, other):
        for x, y in zip(self.value, other.value):
            if isinstance(x, list) or isinstance(y, list):
                tmp = self.compare_lists(x, y)
                if tmp != None:
                    return tmp
            else:
                # integers
                if x > y:
                    return False
                elif x < y:
                    return True

        # correct order apart from length
        if len(self.value) > len(other.value):
            return False
        elif len(self.value) < len(other.value):
            return True
        else:
            return ValueError("Packete gleichwertig, sollte nicht vorkommen !!!")

    def __str__(self) -> str:
        return f"{self.value}"

    def compare_lists(self, first, second):
        if not isinstance(first, list):
            first = [first]
        elif not isinstance(second, list):
            second = [second]

        for x, y in zip(first, second):
            if isinstance(x, list) or isinstance(y, list):
                tmp = self.compare_lists(x, y)
                if tmp != None:
                    return tmp
            else:
                if x > y:
                    return False
                elif x < y:
                    return True

        # same apart from length
        if len(first) > len(second):
            return False
        elif len(first) < len(second):
            return True
        else:
            return None

def compare(input):
    first = Packet(eval(input[0]))
    second = Packet(eval(input[1]))

    return first < second


def part1(input):
    start = time()
    result = 0

    index = 1
    for i in range(0, len(input), 3):
        result += index * compare(input[i:i + 2])
        index += 1

    end = time()
    print(f"Part 1: {result}\t{end - start}")

def part2(input):
    start = time()

    packets = []
    for i in range(0, len(input), 3):
        packets.append(Packet(eval(input[i])))
        packets.append(Packet(eval(input[i + 1])))
    packets.append(Packet([[2]]))
    packets.append(Packet([[6]]))

    result = 1
    packets.sort()
    for index, packet in enumerate(packets):
        if (packet.value == [[2]]) or (packet.value == [[6]]):
            result *= (index + 1
            )
    end = time()
    print(f"Part 2: {result}\t{end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
