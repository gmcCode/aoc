import utils
from typing import List, Tuple
import sys
import re
from time import perf_counter

def interpret_input(input: List[str]) -> Tuple[str, str]:
    for line in input:
        tmp = re.sub("([a-z]{4})", r"\1()", line)
        if "root():" in tmp:
            result = tmp.split(": ")[1].split(" + ")
            continue
        tmp = "def " + tmp.replace(":", ": return")
        exec(tmp, globals())
    return result

def get_const_expr(expressions):
    tmp = f"def humn(): raise ValueError"
    exec(tmp, globals())
    try:
        eval(expressions[0])
    except ValueError:
        return 1, 0
    try:
        eval(expressions[1])
    except ValueError:
        return 0, 1

def part1(input):
    start = perf_counter()
    interpret_input(input)

    print(f'Part 1: {int(root())}')
    end = perf_counter()
    print(f"Time: {end - start}")


def part2(input):
    start = perf_counter()
    expr = interpret_input(input)
    const, var = get_const_expr(expr)
    const = eval(expr[const])

    first = 0
    last = 5000000000000

    tmp = f"def humn(): return {first}"
    exec(tmp, globals())
    result = eval(expr[var])

    while(const != result):
        mid = (first + last) // 2
        tmp = f"def humn(): return {mid}"
        exec(tmp, globals())
        
        result = eval(expr[var])
        if result < const:
            last = mid
        else:
            first = mid
        

    print(f'Part 2: {mid}')
    end = perf_counter()
    print(f"Time: {end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    # part1(input)
    part2(input)
