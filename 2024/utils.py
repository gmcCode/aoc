#!/usr/bin/env python3
import inspect
import timeit
from pathlib import Path


def get_input_as_lines(test=True):
    parent = Path(inspect.stack()[1].filename)
    day = parent.stem

    if test:
        filename = "./inputs/" + day + "_test.txt"
    else:
        filename = "./inputs/" + day + ".txt"

    input = []
    with open(Path(filename), "r", encoding="utf8") as file:
        for line in file:
            input.append(line.rstrip())
    return input


def timed_execution(function, input, number=1000):
    setup_code = f"from __main__ import {function.__name__}, input"
    test_code = f"{function.__name__}(input)"
    exec_time_ms = timeit.timeit(
        test_code, setup=setup_code, number=number, globals=globals()) / number

    print(f"\n{function.__name__}: {function(input)}")
    print(f"Runtime: {exec_time_ms * 1000} ms")
