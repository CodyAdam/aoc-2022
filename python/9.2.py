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

t = [(0, 0)] * 10
visited = set([(0, 0)])

for line in file.splitlines():
    direction, count = line.split()
    count = int(count)

    for _ in range(count):
        dx, dy = DIR[direction]
        t[0] = (t[0][0] + dx, t[0][1] + dy)
        for i in range(9):
            hx, hy, tx, ty = move_tail(*t[i], *t[i + 1])
            t[i] = (hx, hy)
            t[i + 1] = (tx, ty)
        visited.add(t[9])
print(len(visited))
