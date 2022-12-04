import sys

try:
    with open("input.txt") as file:
        file = file.read()
except:
    with sys.stdin as file:
        file = file.read()

lines = [line.strip() for line in file.splitlines()]
# subList = [theList[n:n+N] for n in range(0, len(theList), N)]

s= 0
for line in lines:
    a, b = line.split(",")
    a = list(map(int, a.split("-")))
    b = list(map(int, b.split("-")))


    a0, a1 = a
    b0, b1 = b

    valid = False
    if b0 >= a0 and b1 <= a1:
        s += 1
        valid = True
    elif a0 >= b0 and a1 <= b1:
        valid = True
        s += 1
    print(a, b, "yes" if valid else "")
print(s)