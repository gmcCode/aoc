import utils
import copy
import re
from operator import add, sub
from time import perf_counter

#list( map(add, list1, list2) )

# tuple(sum(x) for x in zip(coord, dir))

class Simulation:
    def __init__(self, line, time) -> None:
        self.blueprint = []
        self.time = time
        self.queue = [self.State([0,0,0,0], [1,0,0,0], time, [False, False, False, False])]
        self.parse_input(line)
        self.most_needed = [max([self.blueprint[i][j] for i in range(4)]) for j in range(4)]
    
    class State:
        def __init__(self, m, r, t, nb) -> None:
            self.materials = m
            self.robots = r
            self.time = t
            self.not_built = nb

    def mine(self, robots, materials):
        return list(map(add, robots, materials))
    
    def build_robot(self, robot_id, materials):
        return list(map(sub, materials, self.blueprint[robot_id]))

    def search_algo(self):
        seen = {}
        reachable = [(i*(i-1))/2 for i in range(self.time + 1)]

        geode_cnt = 0
        while self.queue:
            state = self.queue.pop()
            if(state.materials[-1] + state.robots[-1] * state.time + reachable[state.time] <= geode_cnt):
                continue
            tmp = (tuple(state.robots), tuple(state.materials))
            if(tmp in seen.keys()):
                if state.time <= seen[tmp]:#not self.greater_list(state.materials, seen[tmp]):
                    continue
            else:
                seen[tmp] = state.time

            if state.time > 2:
                if self.materials_check(state.materials, 3):
                    m = self.mine(state.robots, state.materials)
                    m = self.build_robot(3, m)
                    r = copy.deepcopy(state.robots)
                    r[3] += 1
                    self.queue.append(self.State(m, r, state.time - 1, [False, False, False, False]))
                    continue
                for robot_id, _ in enumerate(self.blueprint[0:3]):
                    if self.materials_check(state.materials, robot_id) and not state.not_built[robot_id] and state.robots[robot_id] < self.most_needed[robot_id]:
                        m = self.mine(state.robots, state.materials)
                        m = self.build_robot(robot_id, m)
                        r = copy.deepcopy(state.robots)
                        r[robot_id] += 1
                        state.not_built[robot_id] = True
                        self.queue.append(self.State(m, r, state.time - 1, [False, False, False, False]))
                # don't build any bot
                m = self.mine(state.robots, state.materials)
                self.queue.append(self.State(m, state.robots, state.time - 1, state.not_built))
            elif state.time == 2:
                m = self.mine(state.robots, state.materials)
                m = self.mine(state.robots, m)
                if self.materials_check(state.materials, 3):
                    geode_cnt = max(geode_cnt, m[-1] + 1)
                else:
                    geode_cnt = max(geode_cnt, m[-1])
        return geode_cnt


    def parse_input(self, line):
        robots = line.split(":")[1].split(".")
        for id, robot in enumerate(robots[0:-1]):
            if id < 2:
                num = re.findall(r'\d+', robot)
                self.blueprint.append([int(num[0]), 0, 0, 0])
            elif id == 2:
                num = re.findall(r'\d+', robot)
                self.blueprint.append([int(num[0]), int(num[1]), 0, 0])
            elif id == 3:
                num = re.findall(r'\d+', robot)
                self.blueprint.append([int(num[0]), 0, int(num[1]), 0])
        pass

    def materials_check(self, materials, robot_id):
        for i in range(len(materials)):
            if materials[i] - self.blueprint[robot_id][i] < 0:
                return False
        return True



def part1(input):
    start = perf_counter()
    summe = 0

    for i, line in enumerate(input):
        s = Simulation(line, 24)
        summe += (i+1) * s.search_algo()
        print(f"Completed Blueprint {i+1}")

    end = perf_counter()
    print(f"Part 1: {summe}")
    print(f"Time: {end - start}")

def part2(input):
    start = perf_counter()
    product = 1

    for i, line in enumerate(input[0:3]):
        s = Simulation(line, 32)
        product *= s.search_algo()
        print(f"Completed Blueprint {i+1}")

    end = perf_counter()
    print(f"Part 2: {product}")
    print(f"Time: {end - start}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
