import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import utils

# A -- Rock
# B -- Paper
# C -- Scissors

# X -- lose
# Y -- draw
# Z -- win


def points_for_shape(me) -> int:
    if me == "A":
        return 1
    elif me == "B":
        return 2
    else:
        return 3


# Hässlich... aber funktioniert
def points_for_result(me, oponent) -> int:
    if me == oponent:
        return 3
    if (
        (me == "A" and oponent == "C")
        or (me == "B" and oponent == "A")
        or (me == "C" and oponent == "B")
    ):
        return 6
    return 0


def shape_for_result(result, oponent):
    return {
        "X": {"A": "C", "B": "A", "C": "B"}, # Lose
        "Y": {"A": "A", "B": "B", "C": "C"}, # Draw
        "Z": {"A": "B", "B": "C", "C": "A"}, # Win
    }[result][oponent]


def part1(input):
    my_points = 0

    for line in input:
        oponent, me = line.split()
        me = chr(ord(me) - 23)
        my_points += points_for_shape(me) + points_for_result(me, oponent)

    print(f"Part 1: {my_points}")


def part2(input):
    my_points = 0

    for line in input:
        oponent, result = line.split()

        # points for the result
        my_points += {"X": 0, "Y": 3, "Z": 6}[result]
        my_points += points_for_shape(shape_for_result(result, oponent))

    print(f"Part 2: {my_points}")

if __name__ == "__main__":
    input = utils.get_input_as_lines(test=True)
    part1(input)
    part2(input)
