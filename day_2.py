import utils
from cmath import pi, exp
from math import atan2

# def evalRound(gegner, ich) -> int:
#     punkte = 0
#     sieg =  ord(ich) - (ord(gegner) + ord('X') - ord('A'))
#     punkte += 3 * (sieg + 1)
#     punkte += (ord(ich) - ord('X') + 1)
#     return punkte



"""
- function which checks if we win depending on {A..C} {X..Z}
- function which calculates resulting points

points
rock: A, X, 1p

paper B, Y, 2p

scissors C, Z, 3p

"""


conversions = {
                "X":"A", # stone
                "Y":"B", # paper
                "Z":"C"  # scissors
              }

numbers = {
            "A" : exp(1j*3/2*pi),
            "B" : exp(1j*1/6*pi),
            "C" : exp(1j*5/6*pi)
          }

def parabola(x):
    # https://www.wolframalpha.com/input?i=parabola+through+%280%2C+3%29%2C+%28120%2C+6%29%2C+%28240%2C+0%29
    return int(- 1 / 3200 * x**2 + 1 / 16 * x + 3)

def calculate_wl_points(me, enemy):
    me = conversions[me]
    me_ = numbers[me]
    enemy = numbers[enemy]
    fraction = me_ / enemy
    ratio = atan2(fraction.imag, fraction.real)
    angle = round(ratio * 180 / pi)
    wl_points = parabola(angle%360)
    return wl_points + list(numbers.keys()).index(me) + 1

#print(calculate_wl_points("X", "C"))
#print(calculate_wl_points("Y", "C"))
#print(calculate_wl_points("Z", "C"))

def part1(input):
    punktzahl = 0
    for line in input:
        hand = line.split()
        punktzahl += calculate_wl_points(hand[1], hand[0])
    print(punktzahl)


def part2(input):
    punktzahl = 0
    for line in input:
        hand = line.split()
        punktzahl += (ord(hand[1]) - ord('X')) * 3
        punktzahl += (((ord(hand[0]) - ord('A')) + (ord(hand[1]) - ord('Y'))) % 3) + 1
    print(punktzahl)

if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
