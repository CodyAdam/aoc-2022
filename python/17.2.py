import time

winds = open("input.txt").read().strip()


def get_spawn(max_y):
    return (2, max_y + 4)


def can_move(block_i, pos, direction, solid_tiles):
    global blocks
    for tile in blocks[block_i]:
        x, y = pos[0] + tile[0] + direction[0], pos[1] + tile[1] + direction[1]
        if (x, y) in solid_tiles or x < 0 or x >= W or y < 0:
            return False
    return True


def move(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def stun(block_i, pos, solid_tiles):
    global blocks
    for tile in blocks[block_i]:
        solid_tiles.add((pos[0] + tile[0], pos[1] + tile[1]))


def show():
    global solid_tiles, max_y, moving
    block_i, pos = moving
    movin_tiles = {(pos[0] + tile[0], pos[1] + tile[1])
                   for tile in blocks[block_i]}

    for y in range(max_y + 9, max(-1, max_y - 20), -1):
        for x in range(W):
            if (x, y) in solid_tiles:
                print("█", end="█")
            elif (x, y) in movin_tiles:
                print("▓", end="▓")
            else:
                print("░", end="░")
        print()
    print("--------------", wind_count % len(winds), block_count)
    time.sleep(.03)


def is_closed():
    global max_y, solid_tiles
    new_solids = set()
    for x in range(W):
        if (x, max_y) in solid_tiles:
            new_solids.add((x, max_y))
        elif (x, max_y - 1) in solid_tiles:
            new_solids.add((x, max_y - 1))
        else:
            return False
    solid_tiles = new_solids
    return True


blocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]

W = 7  # width grid
# infinite height

solid_tiles = set()
max_y = -1
moving = (0, get_spawn(max_y))
wind_count = 0
block_count = 0
cache = {}
has_loop = False

while block_count < 1000000000000:
    # Apply wind
    block_i, pos = moving
    wind = winds[wind_count % len(winds)]
    wind_count += 1
    if wind == "<":
        direction = (-1, 0)
    else:
        direction = (1, 0)
    if can_move(block_i, pos, direction, solid_tiles):
        moving = (block_i, move(pos, direction))
    # show()

    # Apply gravity
    block_i, pos = moving
    if can_move(block_i, pos, (0, -1), solid_tiles):
        moving = (block_i, move(pos, (0, -1)))
    else:
        stun(block_i, pos, solid_tiles)
        max_y = max(solid_tiles, key=lambda x: x[1])[1]
        moving = ((block_count + 1) % len(blocks), get_spawn(max_y))
        block_count += 1
        if is_closed():
            top2rows_relative = tuple([(x, y - max_y) for x, y in solid_tiles
                                       if y >= max_y - 1])
            c = (moving[0], top2rows_relative, wind_count % len(winds))
            show()
            if not has_loop:
                if c in cache:
                    print("Loop detected")
                    has_loop = True
                    block_count_loop, max_y_loop = cache[c]
                    bc_to_add = block_count - block_count_loop
                    max_y_to_add = max_y - max_y_loop
                    left = 1000000000000 - block_count
                    block_count += (left // bc_to_add) * bc_to_add
                    max_y += (left // bc_to_add) * max_y_to_add
                    new_solids = set()
                    for x, y in solid_tiles:
                        new_solids.add(
                            (x, y + (left // bc_to_add) * max_y_to_add))
                    solid_tiles = new_solids
                    moving = ((block_count) % len(blocks), get_spawn(max_y))
                    show()
                else:
                    cache[c] = (block_count, max_y)
    # show()
print(max_y + 1)