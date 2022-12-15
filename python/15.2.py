import re
from collections import defaultdict

file = open("input.txt").read()

beac2sens = defaultdict(list)
sens2beac = {}

for line in file.splitlines():
    regex = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    sx, sy, bx, by = re.findall(regex, line)[0]
    beacon = (int(bx), int(by))
    sensor = (int(sx), int(sy))
    sens2beac[sensor] = beacon
    beac2sens[beacon].append(sensor)


def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_range_without_beacon_on_line(y, s, b):
    sx, sy = s
    dist = manhattan_dist(s, b)
    diff_to_y = abs(sy - y)
    miniX = sx + (dist - diff_to_y)
    maxiX = sx - (dist - diff_to_y)
    return (miniX, maxiX)

def overlap(x, y):
    if not is_overlapping(x, y):
        return set()
    return set(range(max(x.start, y.start), min(x.stop, y.stop)+1))

def is_overlapping(x, y):
    if x.start == x.stop or y.start == y.stop:
        return False
    return x.start <= y.stop and y.start <= x.stop

def merge_range(ranges: list[set]):
    # format is : [(min, max), (min, max), ...]
    final_range = []
    has_changed = True
    while has_changed:
        has_changed = False
        for mini1, maxi1 in ranges:

            for mini2, maxi2 in ranges:
                if has_changed:
                    break
                if (mini1 <= mini2 and mini2 <= maxi1) and (mini2 <= maxi1 and
                                                            maxi1 <= mini2):
                    final_range.append((mini1, maxi2))
                    has_changed = True
            if has_changed:
                break
            else:
                final_range.append((mini1, maxi1))

    return final_range


blocked = set()
print(len(blocked) - 1)

for y in range(0 + 1):
    ranges = []
    for s in sens2beac:
        b = sens2beac[s]
        ranges.append(get_range_without_beacon_on_line(y, s, b))
    print(ranges)

print("done")