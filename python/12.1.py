file = open("input.txt").read()
grid = [[ord(char) for char in list(line)] for line in file.splitlines()]
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == ord("S"):
            start = (x, y)
            grid[y][x] = ord("a")
        if grid[y][x] == ord("E"):
            end = (x, y)
            grid[y][x] = ord("z")
grid = list(map(lambda line: list(map(lambda val: val - ord("a"), line)),
                grid))


def show():
    global grid
    print("BOARD ----- ")
    for yy in range(len(grid)):
        for xx in range(len(grid[yy])):
            if (xx, yy) == start:
                print("{:>3}".format("█S█"), end="")
            elif (xx, yy) == end:
                print("{:>3}".format("█E█"), end="")
            else:
                print("{:>3}".format(grid[yy][xx]), end="")
        print()


def get_min_neigh(pos):
    global grid, dist
    x, y = pos
    mini = dist[y][x]
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if x + dx < 0 or x + dx >= len(grid[y]):
            continue
        if y + dy < 0 or y + dy >= len(grid):
            continue
        if grid[y + dy][x + dx] + 1 >= grid[y][x]:
            mini = min(mini, dist[y + dy][x + dx] + 1)
    return mini


dist = [[99999 for _ in range(len(grid[y]))] for y in range(len(grid))]
x, y = start
nodes = [start]
dist[y][x] = 0
ite = 0
show()
while (len(nodes)):
    ite += 1
    pos = nodes.pop(0)
    x, y = pos
    value = grid[y][x]
    dist[y][x] = get_min_neigh(pos)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if x + dx < 0 or x + dx >= len(
                grid[y]) or y + dy < 0 or y + dy >= len(grid):
            continue
        next_value = grid[y + dy][x + dx]
        new_pos = (x + dx, y + dy)
        if next_value <= value + 1 and dist[y + dy][
                x + dx] > dist[y][x] + 1 and new_pos not in nodes:
            nodes.append(new_pos)

print("DISTS ----- ")
for yy in range(len(grid)):
    for xx in range(len(grid[yy])):
        if dist[yy][xx] != 99999:
            print("{:>3}".format(dist[yy][xx]), end="")
        else:
            print("{:>3}".format("███"), end="")
    print()
print(dist[end[1]][end[0]], ite)