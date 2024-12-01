import utils

def get_calories_per_elf(input):
    elves = [0]
    i = 0
    for calories in input:
        if calories == "":
            i = i + 1
            elves.append(0)
        else:
            elves[i] += int(calories)
    return elves


def max(elves):
    a = 0
    for i in range(0, len(elves)):
        if elves[a] < elves[i]:
            a = i
    print(elves[a])


def top3(elves):
    top = [0] * 3
    for i in range(0, len(elves)):
        if top[0] < elves[i]:
            top[0] = elves[i]
            top.sort()
    maxall = top[0] + top[1] + top[2]
    print(maxall)


def part1(input):
    elves = get_calories_per_elf(input)
    print("Part 1:")
    max(elves)


def part2(input):
    elves = get_calories_per_elf(input)
    print("\nPart 2:")
    top3(elves)


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
