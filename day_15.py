import utils
import re
from time import time

def readData(line):
    sensor, beacon = line.split(":")
    sensor = re.split('[,=]', sensor)[1:4:2]
    sensor = tuple(map(int, (x for x in sensor)))
    beacon = re.split('[,=]', beacon)[1:4:2]
    beacon = tuple(map(int, (x for x in beacon)))

    return sensor, beacon
        
def calc_manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def part1(input, y = 2000000):
    occupied = set()
    for line in input:
        sensor, bacon = readData(line)
        dist = calc_manhattan_dist(sensor, bacon)
        ahm = dist - abs(y-sensor[1])
        if ahm > 0:
            for x in range(sensor[0] - ahm, sensor[0] + ahm + 1, 1):
                occupied.add(x)

    for line in input:
        _, bacon = readData(line)
        if bacon[1] == y and bacon[0] in occupied:
            occupied.remove(bacon[0])

    print(f"Part 1: {len(occupied)}")
    


def part2x(input):
    size = 4000000
    for y in range(size+1):
        free = []
        for [x1, y1, x2, y2] in sensors:
            dist = abs(x1 - x2) + abs(y1 - y2)
            tmp = dist - abs(y1 - y)
            if tmp > 0:
                free.append([x1 - tmp, x1 + tmp])  # abs(x-x1) + abs(y1-y_row) <= dist
        free.sort() #sortiert magischerweise nach der ersten Stelle
        mega_smart_intervals = [free[0]] #hat bestimmt nicht lange gedauert und setzt auch nicht dreist voraus das elems in free sind
        for lower_b, upper_b in free:
            tmp_high = mega_smart_intervals[-1][1]
            if lower_b > tmp_high + 1:
                print(f"Part 2: {(tmp_high+1) * 4000000 + y}")
                #mega_smart_intervals.append([lower_b, upper_b])
                return
            if(max(tmp_high, upper_b) < size):
                mega_smart_intervals[-1][1] = max(tmp_high, upper_b)
            else:
                break

        #jetzt schauen wir ob alle x_coords in diesen coolen Intervalen liegen
        # x = 0
        # for lower_b, upper_b in mega_smart_intervals:
        #     if x < lower_b:
        #         print(f"Part 2: {x * 4000000 + y}")
        #         return #wie stoppe ich hier Lars? so?
        #     x = max(x, upper_b + 1)
        #     if x > size:
        #         break

def convert(x, y):
    return -x+y, x+y

def convertback(x, y):
    return (y-x)/2, (x+y)/2

def part2(input):
    left, right, up, bottom = [], [], [], []
    for [x1, y1, x2, y2] in input:
        dist = abs(x1 - x2) + abs(y1 - y2)
        left.append((convert(x1, y1 - dist), 2*dist))
        right.append((convert(x1 - dist, y1), 2*dist))
        up.append((convert(x1 + dist, y1), 2*dist))
        bottom.append((convert(x1, y1 - dist), 2*dist))
    parallels_s, parallels_r = [], []
    for ((s1, r1), length1) in left:
        for ((s2, r2), length2) in right:
            if s1 - s2 == 2:
                if r1 <= r2 <= r1 + length1:
                    parallels_s.append((s1, r2, min(length2, r1 + length1 - r2)))
                elif r2 <= r1 <= r2 + length2:
                    parallels_s.append((s1, r1, min(length1, r2 + length2 - r1)))
    for ((s1, r1), length1) in bottom:
        for ((s2, r2), length2) in up:
            if r1 - r2 == 2:
                if s1 <= s2 <= s1 + length1:
                    parallels_r.append((r1, s2, min(length2, s1 + length1 - s2)))
                elif s2 <= s1 <= s2 + length2:
                    parallels_r.append((r1, s1, min(length1, s2 + length2 - s1)))

    for (s1, r1, length1) in parallels_s:
        for (r2, s2, length2) in parallels_r:
            if r1 <= r2 <= r1 + length1 and s2 <= s1 <= s2 + length2 \
                    and r1 <= r2 - 2 <= r1 + length1 and s2 <= s1 - 2 <= s2 + length2:
                solution = convertback(s1 - 1, r2 - 1)
                print(solution[0]*4000000+solution[1])
                return


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    sensors = []
    for line in input:
        a = line.split('=')
        a = list(map(int, [a[1].split(',')[0], a[2].split(':')[0], a[3].split(',')[0], a[4]]))
        sensors.append(a)

    start = time()
    part1(input)
    ende = time()
    print(f"Laufzeit Part 1: {ende - start}")

    start = time()
    part2(sensors)
    ende = time()
    print(f"Laufzeit Part 2: {ende - start}")