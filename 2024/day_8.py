from utils import *

def getAntennas(input):
    antennas = []
    for c in range(len(input)): 
        for r in range(len(input[c])):
            if '.' in input[c][r]:
                continue
            else:
                pos = (c,r) 
                arrayPos = getAntennaArray(input,c,r,antennas)
                if(arrayPos != -1):
                    antennas[arrayPos].append(pos)
                else:
                    antennas.append([])
                    antennas[-1].append(input[c][r])
                    antennas[-1].append(pos)
    return antennas

def antinodespart1(antennas,frequence):
    antinodes = set()
    for larsA in range(1,len(antennas[frequence])):
        for larsB in range(larsA + 1,len(antennas[frequence])):
            deltax = (antennas[frequence][larsA][0]-antennas[frequence][larsB][0])
            deltay = (antennas[frequence][larsA][1]-antennas[frequence][larsB][1])
            pos1 = (antennas[frequence][larsA][0] - deltax, antennas[frequence][larsA][1] - deltay)
            if(pos1[0] == antennas[frequence][larsB][0] and pos1[1] == antennas[frequence][larsB][1]):
               pos1 = (antennas[frequence][larsA][0] + deltax, antennas[frequence][larsA][1] + deltay)

            pos2 = (antennas[frequence][larsB][0] - deltax, antennas[frequence][larsB][1] - deltay)
            if(pos2[0] == antennas[frequence][larsA][0] and pos2[1] == antennas[frequence][larsA][1]):
                pos2 = (antennas[frequence][larsB][0] + deltax, antennas[frequence][larsB][1] + deltay)

            if pos1[0] <= len(input[0]) -1 and pos1[0] >= 0 and pos1[1] <= len(input)-1 and pos1[1] >=0:
                antinodes.add(pos1)
            if pos2[0] <= len(input[0]) -1 and pos2[0] >= 0 and pos2[1] <= len(input)-1 and pos2[1] >=0:
                antinodes.add(pos2)
    return antinodes   
 
def antinodespart2(antennas,frequence):
    antinodes = set()
    for larsA in range(1,len(antennas[frequence])):
        for larsB in range(larsA + 1,len(antennas[frequence])):
            deltax = (antennas[frequence][larsA][0]-antennas[frequence][larsB][0])
            deltay = (antennas[frequence][larsA][1]-antennas[frequence][larsB][1])
            laufLars = 0
            pos = antennas[frequence][larsA]
            while pos[0] <= len(input[0])-1 and pos[0] >= 0 and pos[1] <= len(input)-1 and pos[1] >=0:
                antinodes.add(pos)
                pos = (antennas[frequence][larsA][0] - laufLars * deltax, antennas[frequence][larsA][1] - laufLars * deltay)
                laufLars += 1
            laufLars = 1
            pos = antennas[frequence][larsA]
            while pos[0] <= len(input[0])-1 and pos[0] >= 0 and pos[1] <= len(input)-1 and pos[1] >=0:
                antinodes.add(pos)
                pos = (antennas[frequence][larsA][0] + laufLars * deltax, antennas[frequence][larsA][1] + laufLars * deltay)
                laufLars += 1
            
    return antinodes   


def antinodespart2shorter(antennas,frequence):
    antinodes = set()
    antennas[frequence].remove(antennas[frequence][0])
    while not antennas[frequence] == []:
        larsA = antennas[frequence].pop()
        for larsB in antennas[frequence]:
            deltax = larsA[0]-larsB[0]
            deltay = larsA[1]-larsB[1]
            pos = larsA
            while pos[0] <= len(input[0])-1 and pos[0] >= 0 and pos[1] <= len(input)-1 and pos[1] >=0:
                antinodes.add(pos)
                pos = (pos[0] - deltax, pos[1] - deltay)
            pos = larsA
            while pos[0] <= len(input[0])-1 and pos[0] >= 0 and pos[1] <= len(input)-1 and pos[1] >=0:
                antinodes.add(pos)
                pos = (pos[0] + deltax, pos[1] + deltay)
            
    return antinodes  
 

def getAntennaArray(input,c,r,antennas):
    for a in range(len(antennas)):
        if input[c][r] in antennas[a]:
            return a
    return -1

def part1(input):
    antennen = getAntennas(input)
    hilfe = set()
    for lars in range(len(antennen)):
        hilfe.update(antinodespart1(antennen,lars))
    return len(hilfe)
   
def part2(input):
    antennen = getAntennas(input)
    hilfe = set()
    for lars in range(len(antennen)):
        hilfe.update(antinodespart2(antennen,lars))
    return len(hilfe)
    
if __name__ == "__main__":
    input = get_input_as_lines(test=True)

    timed_execution(part1, input)
    timed_execution(part2, input)

