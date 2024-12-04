from utils import *


def countXmas(input: str) -> int:
    count = 0

    return count


def part1(input):
    result = 0
    y = 0
    characters = []
    for line in input:
        characterinline = []
        for i in range(len(line)):
            characterinline.append(line[i])
        characters.append(characterinline)

    # print(characters)

    coords = []
    for character in characters:
        for i in range(len(character)):
            x = character[i]
            if x == "X":
                pos = [i, y]
                coords.append(pos)
        y += 1

    for i in range(len(coords)):
        x = coords[i][0]
        y = coords[i][1]
        # Nach rechts
        if x < len(characters[0]) - 3:
            if (
                characters[y][x + 1] == "M"
                and characters[y][x + 2] == "A"
                and characters[y][x + 3] == "S"
            ):
                result += 1
        # Nach links
        if x > 2:
            if (
                characters[y][x - 1] == "M"
                and characters[y][x - 2] == "A"
                and characters[y][x - 3] == "S"
            ):
                result += 1
        # Nach oben
        if y > 2:
            if (
                characters[y - 1][x] == "M"
                and characters[y - 2][x] == "A"
                and characters[y - 3][x] == "S"
            ):
                result += 1
        # Nach unten
        if y < len(characters) - 3:
            if (
                characters[y + 1][x] == "M"
                and characters[y + 2][x] == "A"
                and characters[y + 3][x] == "S"
            ):
                result += 1
        # Nach rechts unten schräg
        if y < len(characters) - 3 and x < len(characters[0]) - 3:
            if (
                characters[y + 1][x + 1] == "M"
                and characters[y + 2][x + 2] == "A"
                and characters[y + 3][x + 3] == "S"
            ):
                result += 1
        # Nach links unten schräg
        if y < len(characters) - 3 and x > 2:
            if (
                characters[y + 1][x - 1] == "M"
                and characters[y + 2][x - 2] == "A"
                and characters[y + 3][x - 3] == "S"
            ):
                result += 1
        # Nach rechts oben schräg
        if x < len(characters[0]) - 3 and y > 2:
            if (
                characters[y - 1][x + 1] == "M"
                and characters[y - 2][x + 2] == "A"
                and characters[y - 3][x + 3] == "S"
            ):
                result += 1
        # Nach links oben schräg
        if x > 2 and y > 2:
            if (
                characters[y - 1][x - 1] == "M"
                and characters[y - 2][x - 2] == "A"
                and characters[y - 3][x - 3] == "S"
            ):
                result += 1
    return result


def part2(input):
    result = 0
    characters = []

    pattern = ["MMSS", "SMMS", "SSMM", "MSSM"]

    for line in input:
        characterinline = list(line)
        characters.append(characterinline)

    for y, line in enumerate(characters):
        for x, char in enumerate(line):
            if char == "A" and 0 < x < len(line)-1 and 0 < y < len(characters)-1:
                neighbors = []
                neighbors.append(characters[y-1][x-1])
                neighbors.append(characters[y+1][x-1])
                neighbors.append(characters[y+1][x+1])
                neighbors.append(characters[y-1][x+1])

                data = "".join(neighbors)
                if data in pattern:
                    result += 1

    return result


if __name__ == "__main__":
    input = get_input_as_lines(test=False)

    timed_execution(part1, input)
    timed_execution(part2, input)
