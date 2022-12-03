import sys

try:
    with open("input.txt") as file:
        file = file.read()
except:
    with sys.stdin as file:
        file = file.read()

lines = [line.strip() for line in file.splitlines()]

pts = {"X": 1, "Y": 2, "Z": 3}


def lose(x):
    if x == "A":
        return "Z"
    elif x == "B":
        return "X"
    elif x == "C":
        return "Y"


def win(x):
    if x == "A":
        return "Y"
    elif x == "B":
        return "Z"
    elif x == "C":
        return "X"


def draw(x):
    if x == "A":
        return "X"
    elif x == "B":
        return "Y"
    elif x == "C":
        return "Z"


s = 0
for line in lines:
    a, b = line.split()

    if b == "X":
        s += pts[lose(a)]
    elif b == "Y":
        s += pts[draw(a)] + 3
    elif b == "Z":
        s += pts[win(a)] + 6

print(s)
