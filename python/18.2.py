lines = open("input.txt").read().splitlines()

grid = {}
for line in lines:
    x, y, z = map(int, line.split(","))
    grid[(x, y, z)] = [1, 1, 1, 1, 1,
                       1]  # top, bottom, left, right, front, back (surface)

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
              (0, 0, -1)]


def bfs(grid, start):
    queue = [start]
    visited = set()
    iterations = 0
    surface = 0
    while queue and iterations < 10000000:
        iterations += 1
        pos = queue.pop(0)
        if pos not in visited:
            visited.add(pos)
            for dire in directions:
                dx, dy, dz = dire
                new_post = (pos[0] + dx, pos[1] + dy, pos[2] + dz)
                if new_post in grid:
                    surface += 1
                    print(surface)
                else:
                    queue.append(new_post)
    return surface


print(bfs(grid, (-1, -1, -1)))