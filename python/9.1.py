file = open("input.txt").read()


def move_tail(hx, hy, tx, ty):
    if (abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
        return hx, hy, tx, ty
    if hx == tx:
        # move vertical
        if hy > ty:
            ty += 1
        else:
            ty -= 1
    elif hy == ty:
        # move horizontal
        if hx > tx:
            tx += 1
        else:
            tx -= 1
    else:
        # move diagonal
        if hx > tx:
            tx += 1
        else:
            tx -= 1
        if hy > ty:
            ty += 1
        else:
            ty -= 1
    return hx, hy, tx, ty


DIR = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}
hx, hy = 0, 0
tx, ty = 0, 0
visited = set([0, 0])

for line in file.splitlines():
    direction, count = line.split()
    count = int(count)

    for _ in range(count):
        dx, dy = DIR[direction]
        hx += dx
        hy += dy
        hx, hy, tx, ty = move_tail(hx, hy, tx, ty)
        visited.add((tx, ty))
print(len(visited))
