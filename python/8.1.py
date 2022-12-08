from collections import defaultdict

file = open("input.txt").read()
lines = file.splitlines()
grid = [[int(x) for x in line] for line in lines]


def isVisible(x, y, relativeTo=-1, dirs=[(-1, 0), (1, 0), (0, -1), (0, 1)]):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return True

    if relativeTo == -1:
        # first call
        value = grid[y][x]
        if x == 0 or x == len(grid[0]) - 1 or y == 0 or y == len(grid) - 1:
            return True
    else:
        value = relativeTo
        if value <= grid[y][x]:
            return False

    for di in dirs:
        if isVisible(x + di[0], y + di[1], value, [di]):
            return True
    return False


s = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if x == 1 and y == 1:
            print("start")
        if isVisible(x, y, -1):
            s += 1

print(s)