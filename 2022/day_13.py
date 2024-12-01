import utils
from time import time

def getData(input):
    leftPackets = []
    rightPackets = []
    count = 1
    for line in input:
        if count % 3 == 1:
            leftPackets.append(line)
        elif count%3 == 2:
            rightPackets.append(line)
        count+=1
    return leftPackets , rightPackets

def comparePackets(leftPacket, rightPacket):
    left = eval(leftPacket)
    right = eval(leftPacket)


def compareSides(leftPackets, rightPackets):
    for Packet in range (0,len(leftPackets)):
        comparePackets(leftPackets[Packet],rightPackets[Packet])
    

def part1(input):
    leftPackets , rightPackets = getData(input)
    compareSides(leftPackets,rightPackets)


def part2(input):
    pass


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=True)
    part1(input)
    part2(input)