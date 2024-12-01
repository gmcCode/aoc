#!/usr/bin/env python3
import inspect
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
