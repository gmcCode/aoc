import utils


def part1(input):
    print("Part 1:")

    leftside = []
    rightside = []
    sum_ = 0

    for line in input:
        x = line.split(" ")
        leftside.append(int(x[0]))
        rightside.append(int(x[1]))

    leftside.sort()
    rightside.sort()

    for i in range(0, len(leftside)):
        diff = leftside[i] - rightside[i]
        sum_ += abs(diff)

    print(sum([abs(left-right) for left, right in zip(leftside, rightside)]))

    print(sum_)


def part2(input):
    print("\nPart 2:")
    leftside = []
    rightside = []

    for line in input:
        x = line.split()
        leftside.append(int(x[0]))
        rightside.append(int(x[1]))

    result = 0
    for x in leftside:
        result += x * rightside.count(x)

    print(result)


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
