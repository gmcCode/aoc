import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import utils
from time import time

class Filesystem:
    def __init__(self, size):
        self.root = self.Folder("/", "")
        self.cwd = self.root
        self.size = size
        self.folders = []

    def contains(self, name):
        for child in self.kids:
            if name == child.name:
                return True
        return False

    def cd(self, name):
        if name == "/":
            self.cwd = self.root
        elif name == "..":
            self.cwd = self.cwd.parent
        else:
            child = self.cwd.get_child(name)
            if child != None:
                self.cwd = self.cwd.get_child(name)

    def insert_stuff(self, list):
        for line in list:
            if "dir" in line:
                self.mkdir(line.split()[1])
            else:
                size, name = line.split()
                self.touch(name, size)

    def mkdir(self, name):
        folder =  self.cwd.insert_folder(name)
        if folder != None:
            self.folders.append(folder)

    def touch(self, name, size):
        self.cwd.insert_file(name, size)

    def get_free_space(self):
        return self.size - self.root.get_size()

    def __str__(self):
        return f"{self.cwd.name}"

    class File:
        def __init__(self, name, size, parent):
            self.name = name
            self.parent = parent
            self.size = int(size)
            self.type = Filesystem.Type.FILE

        def __str__(self):
            return f"{self.name} ({self.size})"

    class Folder:
        def __init__(self, name, parent):
            self.name = name
            self.parent = parent
            self.kids = []
            self.type = Filesystem.Type.DIR

        def insert_folder(self, name):
            if not self.contains(name):
                folder = Filesystem.Folder(name, self)
                self.kids.append(folder)
                return folder
            else:
                print(f"'{self.name}' already contains '{name}'!")
                return None

        def insert_file(self, name, size):
            if not self.contains(name):
                self.kids.append(Filesystem.File(name, size, self))
            else:
                print(f"'{self.name}' already contains '{name}'!")
            pass

        def contains(self, name):
            for child in self.kids:
                if name == child.name:
                    return True
            return False

        def get_child(self, name):
            if self.contains(name):
                for child in self.kids:
                    if name == child.name:
                        return child
            else:
                print(f"Error in 'get_child': {self.name} doesn't contain '{name}'")
                return None

        def get_size(self):
            size = 0
            for child in self.kids:
                if child.type == Filesystem.Type.FILE:
                    size += child.size
                elif child.type == Filesystem.Type.DIR:
                    size += child.get_size()
            return size

    class Type:
        FILE = 0
        DIR = 1

def build_fs(input):
    fs = Filesystem(70000000)

    # parse input
    for i in range(len(input)):
        line = input[i]
        if "$ cd" in line:
            fs.cd(line.split()[2])
        elif "$ ls" in line:
            end = len(input)
            for j in range(i + 1, len(input)):
                if "$" in input[j]:
                    end = j
                    break
            fs.insert_stuff(input[i + 1:end])

    return fs

def part1(fs):
    sum = 0
    for folder in fs.folders:
        size = folder.get_size()
        if size <= 100000:
            sum += size

    print(f"Part 1: {sum}")


def part2(fs: Filesystem):
    free_space = fs.get_free_space()
    needed_space_for_update = 30000000
    needed_space = needed_space_for_update - free_space


    old_size = float("inf")
    for folder in fs.folders:
        size = folder.get_size()
        if size >= needed_space and size < old_size:
            old_size = size
    
    print(f"Part 2: {old_size}")

if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    start = time()
    fs = build_fs(input)
    part1(fs)
    end = time()
    print(f"{end-start}")
    part2(fs)
