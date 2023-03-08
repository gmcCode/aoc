import utils
import re
import copy
from collections import defaultdict
from itertools import combinations
from time import time

class Valve:
    def __init__(self, id, rate, tunnels_to) -> None:
        self.id = id
        self.rate = rate
        self.neighbors = defaultdict(lambda: float('inf'))
        for valve in tunnels_to:
            self.neighbors[valve] = 1
        self.neighbors[id] = 0

def get_verteces(input):
    verteces = {}
    for line in input:
        tmp = line.split(";")
        start = tmp[0].split(" ", 2)[1]
        rate = int(tmp[0].split("=")[-1])
        end = tmp[1].split("valve")[-1]
        end = re.split('s |, | ', end)[1::]
        verteces[start] = Valve(start, rate, end)
    
    return verteces


def update_pathsss(verteces): #broken vgl. eine Funktion tiefer
    # Floyd-Warshall algorithm
    for valve in verteces.values():
        for target_id in verteces.keys():
            for neighbor_id in verteces.keys():
                tmp = valve.neighbors[neighbor_id] + verteces[neighbor_id].neighbors[target_id]
                if valve.neighbors[target_id] > tmp:
                    valve.neighbors[target_id] = tmp

def update_paths(verteces):
    # Floyd-Warshall algorithm
    for n1 in verteces.values():
        for n2 in verteces.values():
            for n3 in verteces.values():
                tmp = n2.neighbors[n1.id] + n1.neighbors[n3.id]
                if n2.neighbors[n3.id] > tmp:
                    n2.neighbors[n3.id] = tmp

def remove_useless_valves(verteces):
    for valve in verteces.values():
        for neighbor_id in verteces.keys():
            if verteces[neighbor_id].rate == 0:
                del valve.neighbors[neighbor_id]
        
        if valve.neighbors[valve.id] != None:
            del valve.neighbors[valve.id]

paths = []
def dfs(vertices, node = "AA", time = 30, visited = []):
    global paths
    node = vertices[node]
    for n in node.neighbors.keys():
        if n in visited:
            continue
        if time - node.neighbors[n] - 1 <= 0:
            continue
        dfs(vertices, n, time - node.neighbors[n] - 1, visited + [n])
    paths.append(visited)


def find_all_paths(vertices, maxtime):
    allpaths=set()
    visited=set()
    def helper(path, timeleft, visited, node = "AA"):
        visited=visited.copy()
        allpaths.add("".join(path))
        node1 = vertices[node]
        for n in node1.neighbors.keys():
            if n in visited:
                continue
            dist = node1.neighbors[n]
            if dist + 1 < timeleft:
                visited.add(node)
                helper(path+[n], timeleft-dist-1, visited, n)
                visited.remove(node)
    helper([], maxtime, visited)
    return allpaths

def eval_path(vertices, p, time = 30):
    flow = 0
    pred = vertices["AA"]
    for i in range(len(p)):
        node = vertices[p[i]]
        time -= (pred.neighbors[node.id] + 1)
        flow += time * node.rate
        pred = node
    
    return flow


def traverse_path(verteces, start, time, score, opened):
    global max_score
    local_score = 0
    opened_valves = copy.deepcopy(opened)
    start = verteces[start]

    # current valve
    if start.id not in opened_valves:
        time -= 1
        local_score += time * start.rate
        opened_valves.add(start.id)

    for valve_id, dist in start.neighbors.items():
        time_left = max(time - dist, 0)
        if time_left <= 0 or score + local_score + time_left < max_score:
            break
        traverse_path(verteces, start=valve_id, time=time_left, score=score + local_score, opened=opened_valves)
    
    if score + local_score > max_score:
        max_score = score + local_score


def traverse_cave(verteces, start = "AA", time = 30):
    global max_score
    start = verteces[start]
    opened_valves = set()


    for valve_id, dist in start.neighbors.items():
        # current valve
        # time_left = time - 1
        # score = time_left * start.rate
        # opened_valves.add(start.id)
        time_left = time
        score = 0

        time_left = max(time_left - dist, 0)
        if time_left <= 0:
            break
        traverse_path(verteces, start=valve_id, time=time_left, score=score, opened=opened_valves)
    
    if score > max_score:
        max_score = score



def part1(input):
    start = time()
    verteces = get_verteces(input)
    update_paths(verteces)
    remove_useless_valves(verteces)

    dfs(vertices = verteces)
    best = max(eval_path(verteces, p, 30) for p in paths)
    print(f"Part 1: {best}")

    end = time()
    print(f"Time: {end - start}")


def eval_path_pair(vertices, pair):
    (a, b) = pair
    if set(a).isdisjoint(set(b)):
        return eval_path(vertices, a, 26) + eval_path(vertices, b, 26)
    return 0


def part2(input):
    global paths
    start = time()
    verteces = get_verteces(input)
    update_paths(verteces)
    remove_useless_valves(verteces)

    paths.clear()
    dfs(vertices = verteces, time = 26)
    pathpressures={}
    for path in paths:
        path_sorted=" ".join(sorted(path))
        if path_sorted not in pathpressures:
            pathpressures[path_sorted]=0
        pathpressures[path_sorted]=max(pathpressures[path_sorted], eval_path(verteces, path, 26))
    
    maxreleased = 0
    for path1 in pathpressures:
        nodes1=path1.split()
        for path2 in pathpressures:
            nodes2=path2.split()
            if not set(nodes1).isdisjoint(set(nodes2)):
                continue
            maxreleased=max(maxreleased, pathpressures[path1]+pathpressures[path2])
    #maxreleased = max(eval_path_pair(verteces, x) for x in combinations(paths, 2))

    print(f"Part 2: {maxreleased}")
    end = time()
    print(f"Time: {end - start}")

if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
