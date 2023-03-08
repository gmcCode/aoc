def load_inputs():
    input = []
    with open('day_5.txt') as f:
        input = [line.strip("\n") for line in f]
    return input

# 1 - 5 - 9 - 13 - 17 - 21 - 25 - 29 - 33
stack = []

def init_stack(num):
    global stack
    stack = []
    for i in range(num):
        stack.append([])
    return stack

def build_stack(input):
    global stack
    num_of_stacks = int(input[-1][-2])
    stack = init_stack(num_of_stacks)
    for line in input[-2::-1]:
        stack_nr = 0
        for i in range(1, len(line) - 1, 4):
            if line[i] != " ":
                stack[stack_nr].append(line[i])
            stack_nr += 1

def move_supply(cnt, src, dst):
    global stack
    for _ in range(cnt):
        tmp = stack[src - 1].pop()
        stack[dst - 1].append(tmp)

def move_supply_in_order(cnt, src, dst):
    global stack
    tmp = []
    for _ in range(cnt):
        tmp.append(stack[src - 1].pop())
    stack[dst - 1].extend(tmp[::-1])

def move_stack(input, inOrder = False):
    for line in input:
        tmp = line.split()
        cnt = int(tmp[1])
        src = int(tmp[3])
        dst = int(tmp[5])
        if inOrder:
            move_supply_in_order(cnt, src, dst)
        else:
            move_supply(cnt, src, dst)

def part1(input):
    result = ""
    delim = input.index("")
    build_stack(input[0:delim])
    move_stack(input[delim + 1::])
    for crate in stack:
        result += crate.pop()
 
    print(f"Part 1: {result}")

def part2(input):
    result = ""
    delim = input.index("")
    build_stack(input[0:delim])
    move_stack(input[delim + 1::], inOrder=True)
    for crate in stack:
        result += crate.pop()
 
    print(f"Part 2: {result}")

if __name__ == "__main__":
    input = load_inputs()
    part1(input)
    part2(input)
