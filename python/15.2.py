import re
from collections import defaultdict

# Parse input
file = open("input.txt").read()
sens2beac = {}
for line in file.splitlines():
    regex = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    sx, sy, bx, by = re.findall(regex, line)[0]
    beacon = (int(bx), int(by))
    sensor = (int(sx), int(sy))
    sens2beac[sensor] = beacon


def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def overlap(x, y):
    return range(min(x.start, y.start), max(x.stop, y.stop))


def is_overlapping(x, y):
    if x.stop + 1 == y.start or y.stop + 1 == x.start:
        return True
    return x.start <= y.stop and y.start <= x.stop


def get_range_without_beacon_on_line(y, s, b) -> range:
    sx, sy = s
    dist = manhattan_dist(s, b)
    diff_to_y = abs(sy - y)
    if diff_to_y > dist:
        return None
    miniX = sx + (dist - diff_to_y)
    maxiX = sx - (dist - diff_to_y)
    return range(min(miniX, maxiX), max(miniX, maxiX))


max_y = 4000000
ranges_per_y = []
# Find all ranges per y
for y in range(max_y + 1):
    if y % 10000 == 0:
        # log per cent
        print("making line ranges:", y / max_y * 100, "%")
    ranges_per_y.append([])
    for s in sens2beac:
        b = sens2beac[s]
        r = get_range_without_beacon_on_line(y, s, b)
        if r is not None and (r.start < max_y or r.stop >= 0):
            ranges_per_y[y].append(range(max(r.start, 0), min(max_y, r.stop)))


# Remove overlaps
for y in range(max_y + 1):
    if y % 10000 == 0:
        # log per cent
        print("removing overlaps:", y / max_y * 100, "%")
    ranges = ranges_per_y[y]
    has_changed = True
    while has_changed:
        has_changed = False
        for r1 in ranges:
            for r2 in ranges:
                if r1 is r2:
                    continue
                if is_overlapping(r1, r2):
                    has_changed = True
                    ranges.remove(r1)
                    ranges.remove(r2)
                    ranges.append(overlap(r1, r2))
                    break
    ranges_per_y[y] = ranges

# Find the only possibility
for y in range(max_y + 1):
    ranges = ranges_per_y[y]
    if len(ranges) != 1:
        x = -1
        for col in range(max_y + 1):
            if all(col not in range(r.start, r.stop + 1) for r in ranges):
                x = col
                break
        print("### Find possible at (x =", x, ", y =", y, ")  ", ranges)
        print("result = ", 4000000 * x + y)