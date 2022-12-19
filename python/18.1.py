lines = open("input.txt").read().splitlines()

grid = {}
for line in lines:
    x, y, z = map(int, line.split(","))
    grid[(x, y, z)] = [1, 1, 1, 1, 1,
                       1]  # top, bottom, left, right, front, back (surface)

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
              (0, 0, -1)]
for cube in grid:
    x, y, z = cube
    surface = grid[cube]
    for index, dire in enumerate(directions):
        dx, dy, dz = dire
        if (x + dx, y + dy, z + dz) in grid:
            surface[index] = 0

sum_surface = 0
for key in grid:
    print(key, grid[key])
    sum_surface += sum(grid[key])
print(sum_surface)