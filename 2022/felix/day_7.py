import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import utils
from time import time



def part1(input):
    start = time()
    path = []
    folder = {}

    for line in input:
        if '$ cd' in line and not '..' in line:
           path.append(line.split()[2])
        elif '$ cd ..' in line:
            path.pop()
        elif '$' not in line and 'dir' not in line:
            key = "".join(path)
            folder[key] = folder.setdefault(key, 0) + int(line.split()[0])
        elif 'dir' in line:
            key = "".join(path)
            folder[key] = folder.setdefault(key, 0)
    
    result = {}
    for path_ in folder.keys():
        for secondPath, secondSize in folder.items():
            if secondPath.startswith(path_):
                result[path_] = result.setdefault(path_, 0) + secondSize

    sum = 0
    for size in result.values():
        if size <= 100000:
            sum += size
    
    print(sum)
    end = time()

    print(f"{end-start}")

        


#def part2(fs: Filesystem):

    
    #print(f"Part 2: {old_size}")

if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
   # part2(input)
