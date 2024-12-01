def load_inputs():
    input = []
    with open('day_3.txt') as f:
        input = [line.rstrip() for line in f]
    return input

def char_to_number(c):
    num = ord(c)
    if num in range(97,123):
        return num-96
    elif num in range(65, 91):
        return num-38

def find_duplicates(comp1, comp2):
    duplicates = set()
    for item in comp1:
        if item in comp2:
            duplicates.add(item)
    return duplicates

def part1(input):
    sum = 0
    for line in input:
        half = int(len(line)/2)
        comp1 = line[0:half]
        comp2 = line[half::]
        duplicates = find_duplicates(comp1, comp2)
        for dup in duplicates:
            sum += char_to_number(dup)

    print(f"Part 1 {sum}")

def part2(input):
    badges = []
    for l in range(0, len(input), 3):
        for char in input[l]:
            if char in input[l+1] and char in input[l+2]:
                badges.append(char)
                break
    
    sum = 0
    for badge in badges:
        sum += char_to_number(badge)
    print(f"Part 2: {sum}")

if __name__ == "__main__":
    input = load_inputs()
    part1(input)
    part2(input)
