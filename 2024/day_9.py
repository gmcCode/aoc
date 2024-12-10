from utils import *
from dataclasses import dataclass


def disk(input):
    for line in range(len(input)):
        id = 0
        disk = []
        for file in range(len(input[line])):
            if file == 0 or file % 2 == 0:
                for i in range(int(input[line][file])):
                    disk.append(id)
                id += 1
            else:
                for x in range(int(input[line][file])):
                    disk.append('.')
    return disk


def defrag(drive):
    defrag = []
    freespace = 0
    while len(drive) > 0:
        if drive[0] != '.':
            defrag.append(drive[0])
            drive.pop(0)
        else:
            if drive[-1] != '.':
                defrag.append(drive[-1])
                drive.pop(0)
                drive.pop()
                freespace += 1
            else:
                drive.pop()
                freespace += 1

    # for i in range(freespace):
    #    defrag.append('.')
    return defrag


def movefile(disk, drive):
    pass


def part1(input):
    summe = 0
    drive = defrag(disk(input))
    for x in range(len(drive)):
        if drive[x] != '.':
           summe += x*drive[x]
    return summe


def part2(input):
    startdrive = disk(input)
    drive = []
    frag = []
    for pos in range(len(startdrive)):
        # print(startdrive[pos],startdrive[pos-1])
        if startdrive[pos] == startdrive[pos-1]:
            frag.append(startdrive[pos])
            # print(frag)
        elif startdrive[pos] != startdrive[pos-1] and frag != []:
            frag.append(startdrive[pos-1])
            drive.append(frag)
            frag = []
        elif startdrive[pos] != startdrive[pos-1] and frag == [] and pos != 0:
            drive.append([startdrive[pos-1]])
    frag.append(startdrive[-1])
    drive.append(frag)

    print(drive)
    return 0


@dataclass
class File:
    id: int
    length: int


def part2dict(input):
    startdrive = {}

    id = 0
    for idx, element in enumerate(input[0]):
        if idx % 2 == 0:
            # file
            startdrive[idx] = File(id=id, length=element)
            id += 1
        else:
            # free
            startdrive[idx] = File(id=-1, length=element)

    return 0


if __name__ == "__main__":
    input = get_input_as_lines(test=True)

    # timed_execution(part1, input, number=10)
    timed_execution(part2dict, input, number=1)
