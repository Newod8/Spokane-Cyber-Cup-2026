import csv
from enum import Enum

class Type(Enum):
    BLUE = 1
    RED = 2
    GREEN = 3
    YELLOW = 4
    PURPLE = 5
    PINK = 6
    GOLD = 7
    SILVER = 8
    BRONZE = 9
    MAGENTA = 10
    RAINBOW = 11
    NEOPOLITAN = 12
    NAVY = 13
    WHITE = 14
    BLACK = 15

typechartfile = open("types.csv", "r")
reader = csv.reader(typechartfile, delimiter=',')

typechart = list(csv.reader(typechartfile, delimiter=','))

i = 0
j = 0

for row in typechart:
    for item in row:
        match item:
            case "2x":
                typechart[i][j] = 2
            case "0.5x":
                typechart[i][j] = 0.5
            case "0x":
                typechart[i][j] = 0
            case "1x":
                typechart[i][j] = 1
        j += 1
        if j > 15: 
            j = 0
    i += 1

for type in range(1, 16):
    for type2 in range(1, 16):
        weaknessescount = 0
        for attackingtype in range(1, 16):
            if int(typechart[attackingtype][type]) * int(typechart[attackingtype][type2]) > 1:
                weaknessescount += 1
        if weaknessescount < 2:
            print(f"{Type(type).name} {Type(type2).name} has {weaknessescount} weaknesses")
