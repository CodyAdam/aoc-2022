from collections import defaultdict

file = open("input.txt").read()
lines = file.splitlines()
grid = [[int(x) for x in line] for line in lines]


def score(x, y, relativeTo=-1, dirs=[(-1, 0), (1, 0), (0, -1), (0, 1)]):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return 0

    s = 1
    if relativeTo == -1:
        # first call
        value = grid[y][x]
        for di in dirs:
            val = score(x + di[0], y + di[1], value, [di])
            s *= 1 if val == 0 else val
        return s
    else:
        value = relativeTo
        if value <= grid[y][x]:
            return 1
        for di in dirs:
            s += score(x + di[0], y + di[1], value, [di])
        return s


s = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if x == 0 and y == 0:
            print("start")
        s[(x, y)] = score(x, y, -1)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        print("{:>3}".format(str(s[(x, y)])), end=" ")
    print()

# max value in dict 
print(max(s.values()))
