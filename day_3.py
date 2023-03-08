import utils

def part1(input):
    points = 0
    for line in input:
        fachA, fachB = line[:len(line)//2], line[len(line)//2:]

        for char in fachA:
            if char in fachB:
                #points += ord(char) - ord("A") + 27
                break

        if char == char.upper():
            points += ord(char) - ord("A") + 27
        else:
            points += ord(char) - ord("a") + 1
    
    print(f"Part 1:  {points}")


def part2(input):
    points = 0
    for group in range(0,len(input),3):
        for char in input[group]:
            if char in input[group+1] and char in input[group+2]:
                break
        if char == char.upper():
            points += ord(char) - ord("A") + 27
        else:
            points += ord(char) - ord("a") + 1

    print(f"Part 2:  {points}")

if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)