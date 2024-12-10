import math
from utils import *


def recursiveTest(final, remaining):
    curr = remaining.pop()
    if (remaining == []):
        if (final == curr):
            return True
        else:
            return False
    if (final % curr != 0):
        return recursiveTest(final-curr, list(remaining))
    else:
        return (recursiveTest(final-curr, list(remaining)) or recursiveTest(final//curr, list(remaining)))


def concatenation(final, remaining):
    curr = remaining.pop()
    if (remaining == []):
        if (final == curr):
            return True
        else:
            return False
    digits_pow = pow(10, (int(math.log10(curr))+1))
    if (final % curr != 0):
        if (final % digits_pow) == curr:
            return concatenation(final-curr, list(remaining)) or concatenation(final//digits_pow, list(remaining))
        else:
            return concatenation(final-curr, list(remaining))
    else:
        if (final % digits_pow) == curr:
            return (concatenation(final-curr, list(remaining)) or concatenation(final//curr, list(remaining))) or concatenation(final//digits_pow, list(remaining))
        else:
            return (concatenation(final-curr, list(remaining)) or concatenation(final//curr, list(remaining)))


def part1(input):
    result = 0
    for line in input:
        equation = line.split(": ")
        final_number = int(equation[0])
        remaining_numbers = list(map(int, equation[1].split()))
        if recursiveTest(final_number, remaining_numbers):
            result += final_number
    return result


def part2(input):
    result = 0
    for line in input:
        equation = line.split(": ")
        final_number = int(equation[0])
        remaining_numbers = list(map(int, equation[1].split()))
        if concatenation(final_number, remaining_numbers):
            result += final_number
    return result


if __name__ == "__main__":
    input = get_input_as_lines(test=True)

    timed_execution(part1, input)
    timed_execution(part2, input)
