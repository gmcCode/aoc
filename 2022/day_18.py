import utils
from time import perf_counter

class Space:
    def __init__(self, dimensions) -> None:             
        self.x = dimensions[0] + 1 + 2
        self.y = dimensions[1] + 1 + 2
        self.z = dimensions[2] + 1 + 2
        self.space = [[[None] * self.z for j in range(self.y)] for i in range(self.x)]
        self.surface_area = 0
    
    def get_neighbors(self, coord):
        result = []
        directions = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
        for dir in directions:
            tmp = tuple(sum(x) for x in zip(coord, dir))
            if 0 <= tmp[0] < self.x and 0 <= tmp[1] < self.y and 0 <= tmp[2] < self.z:
                result.append(tmp)
        return result

    def insert_rock(self, coord):
        x, y, z = coord
        self.space[x + 1][y + 1][z + 1] = 6

    def get_coord_info(self, coord):
        x, y, z = coord
        return self.space[x][y][z]
    
    def set_coord_info(self, coord, value):
        x, y, z = coord
        self.space[x][y][z] = value

    def update_surface_value(self):
        # doppelt, aber vllt fur Part 2 hilfreich
        for x in range(1, len(self.space)):
            for y in range(1, len(self.space[0])):
                for z in range(1, len(self.space[0][0])):
                    if self.space[x][y][z] != None:
                        cnt = 0
                        if self.space[x + 1][y][z] != None:
                            cnt += 1
                        if self.space[x - 1][y][z] != None:
                            cnt += 1
                        if self.space[x][y + 1][z] != None:
                            cnt += 1
                        if self.space[x][y - 1][z] != None:
                            cnt += 1
                        if self.space[x][y][z + 1] != None:
                            cnt += 1
                        if self.space[x][y][z - 1] != None:
                            cnt += 1
                        self.space[x][y][z] -= cnt
                        self.surface_area += self.space[x][y][z]


def max_dimensions(input):
    dimensions = [0, 0, 0]
    for line in input:
        for id, num in enumerate(line.split(",")):
            dimensions[id] = max(dimensions[id], int(num))
    return dimensions


def part1(input):
    start = perf_counter()
    s = Space(max_dimensions(input))

    for line in input:
        s.insert_rock((int(d) for d in line.split(",")))
    s.update_surface_value()
    print(f"Part 1: {s.surface_area}")
    end = perf_counter()

    print(f"Time: {end - start}")

def part2(input):
    start = perf_counter()
    directions = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
    s = Space(max_dimensions(input))

    for line in input:
        s.insert_rock((int(d) for d in line.split(",")))

    count = 0
    queue = [(0,0,0)]
    s.set_coord_info((0,0,0), 1)
    while queue:
        coord = queue.pop(0)
        for n in s.get_neighbors(coord):
            if s.get_coord_info(n) == 6:
                count += 1
            elif s.get_coord_info(n) == None:
                queue.append(n)
                s.set_coord_info(n, 1)

    
    print(f"Part 2: {count}")
    end = perf_counter()
    print(f"Time: {end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
