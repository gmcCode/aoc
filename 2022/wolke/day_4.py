def load_inputs():
    input = []
    with open('day_4.txt') as f:
        input = [line.rstrip() for line in f]
    return input

def range_subset(range1 , range2):
    """Whether range1 is a subset of range2"""
    if not range1:
        return True     # empty range is subset of anything
    if not range2:
        return False    # non-empty range can´t be subset of empty
    return range1.start in range2 and range1[-1] in range2

def range_overlap(range1, range2):
    return range_subset(range1, range2) or range_subset(range2, range1)

def range_partial_overlap(range1, range2):
    return (range1.start in range2
            or range1[-1] in range2
            or range2.start in range1
            or range2[-1] in range1
            )

def line_to_ranges(line):
    part1, part2 = line.split(",")
    r1_start, r1_end = part1.split("-")
    r2_start, r2_end = part2.split("-")
    range1 = range(int(r1_start), int(r1_end) + 1)
    range2 = range(int(r2_start), int(r2_end) + 1)
    return (range1, range2)

def part1(input):
    sum = 0
    for line in input:
        range1, range2 = line_to_ranges(line)
        if range_overlap(range1, range2):
            sum += 1

    print(f"Part 1: {sum}")

def part2(input):
    sum = 0
    for line in input:
        range1, range2 = line_to_ranges(line)
        if range_partial_overlap(range1, range2):
            sum += 1
    print(f"Part 2: {sum}")

if __name__ == "__main__":
    input = load_inputs()
    part1(input)
    part2(input)
