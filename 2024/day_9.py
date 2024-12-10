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
    result = 0
    startdrive = []

    id = 0
    for idx, element in enumerate(input[0]):
        if idx % 2 == 0:
            # file
            startdrive.append(File(id=id, length=int(element)))
            id += 1
        else:
            # free
            startdrive.append(File(id=-1, length=int(element)))

    revFileIdx = 0
    while revFileIdx < len(startdrive):
        fileIdx = len(startdrive) - 1 - revFileIdx
        if startdrive[fileIdx].id != -1:
            freeIdx = 0
            while freeIdx < fileIdx:
                if startdrive[freeIdx].id == -1 and startdrive[freeIdx].length >= startdrive[fileIdx].length:
                    offset = 0
                    if startdrive[fileIdx].length < startdrive[freeIdx].length:
                        startdrive.insert(
                            freeIdx + 1, File(id=-1, length=startdrive[freeIdx].length-startdrive[fileIdx].length))
                        offset = 1
                    startdrive[freeIdx] = startdrive[fileIdx + offset]
                    startdrive[fileIdx + offset] = File(
                        id=-1, length=startdrive[fileIdx + offset].length)
                    break
                freeIdx += 1
        revFileIdx += 1

    position = 0
    for file in startdrive:
        if file.id != -1:
            result += (position * file.length +
                       ((file.length-1)*file.length)//2) * file.id
        position += file.length
    return result


def part2lists(input):
    result = 0
    files = []
    gaps = []

    pos = 0
    id = 0
    for idx, element in enumerate(input[0]):
        if idx % 2 == 0:
            # file
            files.append([pos, int(element), id])
            id += 1
        else:
            # free
            gaps.append([pos, int(element)])
        pos += int(element)

    for file in reversed(files):
        for gap in gaps:
            if gap[0] > file[0]:
                break
            if gap[1] >= file[1]:
                file[0] = gap[0]
                if gap[1] == file[1]:
                    gaps.remove(gap)
                else:
                    gap[0] += file[1]
                    gap[1] -= file[1]
                break

    for file in files:
        result += (file[0] * file[1] +
                   ((file[1]-1)*file[1])//2) * file[2]
    return result

if __name__ == "__main__":
    input = get_input_as_lines(test=False)

    timed_execution(part1, input, number=10)
    timed_execution(part2dict, input, number=1)
    timed_execution(part2lists, input, number=10)
