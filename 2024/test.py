import re

input = [
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]


def part1Regex(input):
    result = 0
    for line in input:
        pattern = re.compile(
            r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
        matches = pattern.findall(line)
        print(matches)

        active = True
        for match in matches:
            if match == "don't()":
                active = False
            elif match == "do()":
                active = True
            else:
                if active:
                    x, y = map(int, match[4:-1].split(","))
                    result += x*y

            # if match[3] == "don't()":
            #     active = False
            # elif match[2] == "do()":
            #     active = True
            # elif active:
            #     sum += int(match[0]) * int(match[1])
    return result


print(part1Regex(input))
