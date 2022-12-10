from collections import defaultdict

file = open("input.txt").read()

def show():
    for line in img:
        for pixel in line:
            if pixel:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()


def check_signal():
    yy = cycle // 40
    if yy >= 6: return
    xx = (cycle) % 40

    if xx in [x - 1, x, x + 1]:
        img[yy][xx] = True


x = 1
cycle = 0
img = [[False] * 40 for _ in range(6)]
check_signal()

for line in file.splitlines():
    command = line.strip().split()
    if len(command) == 2:
        value = command[1]
        command = command[0]

    # Noop
    if len(command) == 1:
        command = command[0]
        cycle += 1

    # AddX
    if command == "addx":
        cycle += 1
        check_signal()
        cycle += 1
        x += int(value)
    check_signal()

show()
