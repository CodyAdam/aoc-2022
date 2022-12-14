import sys

file = open("input.txt").read()

grid = set()
max_floor = -999
for line in file.splitlines():
    pts = [list(map(int, pt.split(","))) for pt in line.split(" -> ")]
    pts.reverse()
    x, y = pts.pop(0)
    while pts:
        max_floor = max(max_floor, y)
        grid.add((x, y))
        targetX, targetY = pts.pop(0)
        while (x, y) != (targetX, targetY):
            if x < targetX:
                x += 1
            elif x > targetX:
                x -= 1
            if y < targetY:
                y += 1
            elif y > targetY:
                y -= 1
            max_floor = max(max_floor, y)
            grid.add((x, y))

spawn = (500, 0)
steps = 0
max_floor += 2
print(max_floor)

while True:
    i = 0
    x, y = spawn
    while True:
        if i > 9999:
            print(steps)
            sys.exit()
        i += 1
        if (x, y + 1) not in grid and y + 1 != max_floor:
            y += 1
            continue
        if (x - 1, y + 1) not in grid and y + 1 != max_floor:
            x -= 1
            y += 1
            continue
        if (x + 1, y + 1) not in grid and y + 1 != max_floor:
            x += 1
            y += 1
            continue
        else:
            if (x, y) == spawn:
                print(steps+1)
                sys.exit()
            grid.add((x, y))
            steps += 1
            break
