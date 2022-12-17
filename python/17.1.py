import time

winds = open("input.txt").read()


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
    global solid_tiles, max_y, moving, block_count, tile_count
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
    print("--------------")
    time.sleep(.04)


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

while block_count < 2022:
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
    show()

    # Apply gravity
    block_i, pos = moving
    if can_move(block_i, pos, (0, -1), solid_tiles):
        moving = (block_i, move(pos, (0, -1)))
    else:
        stun(block_i, pos, solid_tiles)
        max_y = max(solid_tiles, key=lambda x: x[1])[1]
        moving = ((block_count + 1) % len(blocks), get_spawn(max_y))
        block_count += 1
    show()
print(max_y+1)
