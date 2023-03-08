import utils
from time import time

def reduce_folder_structure(dater):
    temp = dater
    global summe
    folder_size = 0
    for key, val in temp.items():
        if type(val) == dict:
            temp = val
            folder_size += reduce_folder_structure(temp)
        else:
            folder_size += int(val)
    if(folder_size <= 100000):
        summe += folder_size
    return folder_size

def part1(input):
    start = time()

    dater={}
    path=[]
    global summe
    summe = 0
    for zeile in input:
        if '$ cd' in zeile and not '..' in zeile:
            name = zeile.split('$ cd ')[1]
            temp = dater
            for folder in path:
                temp = temp[folder]
            path.append(name)
            temp[name] = {}
        elif '..' in zeile:
            path = path[:-1]
        elif not "dir" in zeile and not "$" in zeile:
            size, name = zeile.split(" ")
            size = int(size)
            temp = dater
            for folder in path:
                temp = temp[folder]
            temp[name] = size

    reduce_folder_structure(dater)
    print(f"Part: 1{summe}")

    end = time()
    print(f"{end-start}")

def reduce_folder_structure2(dater):
    temp = dater
    global summe
    folder_size = 0
    for key, val in temp.items():
        if type(val) == dict:
            temp = val
            print(temp)
            folder_size += reduce_folder_structure(temp)
        else:
            folder_size += int(val)
    if(folder_size <= 100000):
        summe += folder_size
    print(folder_size)
    return folder_size

def part2(input):
    pass


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    # part2(input)