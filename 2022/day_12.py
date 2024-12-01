import utils
from time import time

start = (0, 0)
ende = (0, 0)
visited = {}


class Node:
    def __init__(self, coords, parent, distance = float('inf'), type = 2) -> None:
        self.coords = coords
        self.parent = parent
        self.neighborhood = []
        self.type = type
        self.distance = distance

    def get_len_path(self):
        parent = self.parent
        cnt = 1
        while parent.type != Node.Type.START:
            cnt += 1
            parent = parent.parent
        return cnt
    
        
    # def __eq__(self, __o: object) -> bool:
    #     return __o == self.parent.coords
    
    def __lt__(self, other):
        return self.distance < other.distance

    class Type:
        START = 0
        END = 1
        NORMAL = 2


def get_neighbors(node, heightmap):
    Y = node[0]
    X = node[1]
    result = [(Y - 1, X), (Y + 1, X), (Y, X - 1), (Y, X + 1)]
    deleted_one = 0

    if node[0] == 0:
        # 1. Spalte
        del result[0]
        deleted_one = 1
    elif node[0] == len(heightmap) - 1:
        # letzte Spalte
        del result[1]
        deleted_one = 1
    if node[1] == 0:
        # 1. Zeile
        del result[2 - deleted_one]
    elif node[1] == len(heightmap[0]) - 1:
        # letzte Zeile
        del result[3 - deleted_one]
    return result


def getHeightMap(input):
    global start, ende, heightmap
    heightmap = [[] for _ in range(len(input))]
    for line in range(len(input)):
        for row in range(len(input[line])):
            height = ord(input[line][row]) - 96
            if height == -13:
                start = Node((line, row), None, float('inf'), Node.Type.START)
                height = 1
            elif height == -27:
                ende = Node((line, row), None, 0, Node.Type.END)
                height = 26
            heightmap[line].append(height)
    return heightmap


def constructGraph(map, node):
    global visited
    newNodes = []
    neighbors = get_neighbors(node.coords, map)
    for neighbor in neighbors:
        if (
            heightmap[node.coords[0]][node.coords[1]]
            - heightmap[neighbor[0]][neighbor[1]]
            <= 1
        ):
            if(neighbor not in visited.keys()):
                newNode = Node(neighbor, node)
                visited[newNode.coords] = newNode
                node.neighborhood.append(newNode)
                newNodes.append(newNode)
            else:
                node.neighborhood.append(visited[neighbor])
    return newNodes






def part1(input):
    global ende
    map = getHeightMap(input)
    queue = []
    visited[ende.coords] = ende
    openNodes = [ende]
    while openNodes != []:
        x = openNodes.pop()
        queue.append(x)
        openNodes += constructGraph(map, x)
    print(len(queue))
    print(len(visited))
    while len(queue) != 0:
        v = queue[0]
        v = min(queue)
        queue.remove(v)
        for u in v.neighborhood:
            if (u.distance > v.distance + 1):
                u.distance = v.distance + 1
                u.parent = v
                
    print(f"Part 1: {visited[start.coords].distance}")

def part2(input):
    nearestStart = start
    map = getHeightMap(input)
    for indexX, row in enumerate(map):
        for indexY, x in enumerate(row):
            if (x == 1) and (indexX, indexY) in visited.keys() and visited[(indexX, indexY)].distance < nearestStart.distance:
                nearestStart = visited[(indexX, indexY)]
    

    print(f"Part 2: {nearestStart.distance}")


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    print(len(input[0]))
    part1(input)
    part2(input)
