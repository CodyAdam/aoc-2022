from collections import defaultdict

lines = open("input.txt").read().splitlines()

grid = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            grid.add((x, y))

CONDITIONS = [([(0, -1), (1, -1), (-1, -1)], (0, -1)),
              ([(0, 1), (1, 1), (-1, 1)], (0, 1)),
              ([(-1, -1), (-1, 0), (-1, 1)], (-1, 0)),
              ([(1, -1), (1, 0), (1, 1)], (1, 0))]


def show(grid):
    minX = min(grid, key=lambda pos: pos[0])[0]
    minY = min(grid, key=lambda pos: pos[1])[1]
    maxX = max(grid, key=lambda pos: pos[0])[0]
    maxY = max(grid, key=lambda pos: pos[1])[1]
    # minX = 0
    # minY = 0
    # maxX = 12
    # maxY = 11
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) in grid:
                print("█", end="█")
            else:
                print(".", end=" ")
        print()

    print("  ")


def first_half(x, y, step):
    founded = False
    for dx, dy in [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]:
        if (x + dx, y + dy) in grid:
            founded = True
            break
    if not founded:
        return (x, y)

    for i in range(step, step + 4):
        founded = False
        checks, dpos = CONDITIONS[i % 4]
        for dx, dy in checks:
            if (x + dx, y + dy) in grid:
                founded = True
                break
        if founded:
            continue
        else:
            dx, dy = dpos
            return (x + dx, y + dy)
    return (x, y)


def second_half(next_grid: dict):
    new_grid = set()
    for pos in next_grid:
        prevs = next_grid[pos]
        if len(prevs) != 1:
            for prev in prevs:
                new_grid.add(prev)
        else:
            new_grid.add(pos)
    return new_grid


show(grid)
for step in range(10):
    next_grid = defaultdict(list)
    for pos in grid:
        new_post = first_half(*pos, step)
        next_grid[new_post].append(pos)
    grid = second_half(next_grid)
    # print(step + 1)
    # show(grid)

minX = min(grid, key=lambda pos: pos[0])[0]
minY = min(grid, key=lambda pos: pos[1])[1]
maxX = max(grid, key=lambda pos: pos[0])[0]
maxY = max(grid, key=lambda pos: pos[1])[1]
L = maxX - minX + 1
H = maxY - minY + 1
print((H * L) - len(grid))