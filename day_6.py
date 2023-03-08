import utils
import time

def part1(input):
    start = time.time()
    input = input[0]
    i = 3
    while (i < len(input)):
        if (input[i] == input[i-1]):
            i += 3
        elif (input[i] == input[i-2] or input[i-2] == input[i-1]):
            i += 2
        elif (input[i] == input[i-3] or input[i-3] == input[i-1] or input[i-3] == input[i-2]):
            i += 1
        else:
            print(f"Part 1: {i+1}")
            break
    
    end = time.time()
    print(f"Time {end-start}")

def part2(input):
    start = time.time()
    input = input[0]
    for i in range(len(input)-14):
        if len(set(input[i:i+14])) == 14:
            print(f"Part 2: {i+14}")
            break
    end = time.time()
    print(f"Time {end-start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)