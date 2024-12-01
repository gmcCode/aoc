import utils
from time import time


def part1(input):
    start = time()
    row_length, col_length = len(list(input[0])), len(input)
    visible_map = [[False for i in range(row_length)] for j in range(col_length)]
    forest = []
    for line in input:
       forest.append([int(x) for x in list(line)])

    # links
    for i in range(col_length):
        highest= forest[i][0]
        visible_map[i][0] = True
        for j in range(1, row_length):
            if forest[i][j] > highest:
                visible_map[i][j] = True
                highest = forest[i][j]
    # rechts
    for i in range(col_length):
        highest = forest[i][-1]
        visible_map[i][-1] = True
        for j in range(row_length - 1, 0, -1):
            if forest[i][j] > highest:
                visible_map[i][j] = True
                highest = forest[i][j]
    # oben
    for i in range(row_length):
        highest = forest[0][i]
        visible_map[0][i] = True
        for j in range(1, col_length):
            if forest[j][i] > highest:
                visible_map[j][i] = True
                highest = forest[j][i]
    # unten
    for i in range(row_length):
        highest = forest[-1][i]
        visible_map[-1][i] = True
        for j in range(col_length - 1, 0, -1):
            if forest[j][i] > highest:
                visible_map[j][i] = True
                highest = forest[j][i]

    summe = 0
    for row in visible_map:
        for elem_ in row:
            if elem_ == True:
                summe += 1
    print(summe)  # Idee Felix, erste & letze auslassen, dann ecken true setzen fehlt
    # print(visible_map)

    end = time()
    print(end - start)


def part2(input):
    row_length, col_length = len(list(input[0])), len(input)
    score = 0
    for y, line in enumerate(input[1:-1]):
        y += 1
        for x, tree in enumerate(line[1:-1]):
            tree = int(tree)
            x += 1

            # rechts
            right = 0
            for neighbor in line[x + 1 : :]:
                if int(neighbor) < tree:
                    right += 1
                elif int(neighbor) >= tree:
                    right += 1
                    break

            # links
            left = 0
            for neighbor in line[x - 1 :: -1]:
                if int(neighbor) < tree:
                    left += 1
                elif int(neighbor) >= tree:
                    left += 1
                    break

            # oben
            up = 0
            for i in range(y - 1, -1, -1):
                neighbor = int(input[i][x])
                if int(neighbor) < tree:
                    up += 1
                elif int(neighbor) >= tree:
                    up += 1
                    break

            # unten
            down = 0
            for i in range(y + 1, len(input)):
                neighbor = int(input[i][x])
                if int(neighbor) < tree:
                    down += 1
                elif int(neighbor) >= tree:
                    down += 1
                    break

            temp = up * down * left * right

            score = max(score, temp)

    print(score)


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    # part2(input)


f = open("inputs/day_8.txt").readlines()
start = time()
v = [[False for x in y.strip()] for y in f]
l = len(f)
for i in range(0, l):
    m = ["/"] * 4
    for j in range(0, l):
        for x, (a, b) in enumerate(((i, j), (i, l - j - 1), (j, i), (l - j - 1, i))):
            if f[a][b] > m[x]:
                v[a][b] = True
                m[x] = f[a][b]
print("Part 1:", sum([sum(x) for x in v]))
end = time()
print(end - start)

highest = 0


def view(r, x):
    result = 0
    for k in r:
        result += 1
        if x(f, k) >= value:
            break
    return result


for i in range(0, l):
    for j in range(0, l):
        value = f[i][j]
        highest = max(
            highest,
            view(range(i + 1, l), lambda f, k: f[k][j])
            * view(range(i - 1, -1, -1), lambda f, k: f[k][j])
            * view(range(j + 1, l), lambda f, k: f[i][k])
            * view(range(j - 1, -1, -1), lambda f, k: f[i][k]),
        )
print("Part 2:", highest)
