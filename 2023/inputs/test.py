import time


def valid(p, s):
    p = p.replace(".", " ")
    v = tuple(len(ss) for ss in p.split())
    return v == s


def arrs(p, s, i, g):
    if g > len(s):
        return 0
    if i == len(p):
        if valid(p, s):
            return 1
        return 0
    if p[i] == "?":
        d = p[:i] + "." + p[i + 1 :]  # replace with .
        h = p[:i] + "#" + p[i + 1 :]  # replace with #
        dv = arrs(d, s, i + 1, g)
        if p[i - 1] == ".":
            hv = arrs(h, s, i + 1, g + 1)
        else:
            hv = arrs(h, s, i + 1, g)
        return dv + hv
    else:
        return arrs(p, s, i + 1, g)


start_time = time.time()
with open("day12.txt") as f:
    ls = [l.split() for l in f.read().splitlines()]

sum = 0
for p, s in ls:
    s = tuple(int(s) for s in s.split(","))
    temp = arrs(p, s, 0, 0)
    print(temp)
    sum += temp
print(sum)

print("--- %s seconds ---" % (time.time() - start_time))
