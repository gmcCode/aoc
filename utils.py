#!/usr/bin/env python3
import inspect


def get_input_as_lines(test=True):
    parent = inspect.stack()[1].filename
    parent = parent.split("/")[-1].split(".")[0]

    if test:
        filename = "inputs/" + parent + "_test.txt"
    else:
        filename = "inputs/" + parent + ".txt"

    input = []
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            input.append(line.rstrip())
    return input
