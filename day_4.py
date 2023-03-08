import utils

def splitInIDs(line) -> list:
    x = []
    for s in line.split(','):
        x += s.split('-')
    for j in range(0,len(x)):                   #zahlenwerte = list(map(int,zahlenwerte))
        x[j] = int(x[j])
    return x


def part1(input):
    points = 0
    for i in input:
        x = splitInIDs(i)
        if (x[0] <= x[2] and x[1] >= x[3]) or (x[0] >= x[2] and x[1] <= x[3]):
            points += 1
    
    print(f"Part 1: {points}")
    

def part2(input):
    points = 0
    for i in input:
        x = splitInIDs(i)
        if not((x[3] < x[0]) or (x[2] > x[1])):
            print(x)
            points += 1
    print(f"Part 2: {points}")

if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)