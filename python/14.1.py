import sys

file = open("input.txt").read()

grid = set()
for line in file.splitlines():
    pts = [list(map(int, pt.split(","))) for pt in line.split(" -> ")]
    pts.reverse()
    x, y = pts.pop(0)
    while pts:
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
            grid.add((x, y))

spawn = (500, 0)
steps = 0

while True:
    i = 0
    x, y = spawn
    while True:
        if i > 9999:
            print(steps)
            sys.exit()
        i += 1
        if (x, y + 1) not in grid:
            y += 1
            continue
        if (x - 1, y + 1) not in grid:
            x -= 1
            y += 1
            continue
        if (x + 1, y + 1) not in grid:
            x += 1
            y += 1
            continue
        else:
            grid.add((x, y))
            steps += 1
            break

