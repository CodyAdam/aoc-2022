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


def get_count_without_beacon_on_line(y, s, b):
    sx, sy = s
    blocked = set([(sx, y)])
    dist = manhattan_dist(s, b)
    diff_to_y = abs(sy - y)
    for i in range(dist - diff_to_y + 1):
        if (sx + i, y) is not b:
            blocked.add((sx + i, y))
        if (sx - i, y) is not b:
            blocked.add((sx - i, y))
    return blocked


blocked = set()
for s in sens2beac:
    b = sens2beac[s]
    blocked |= get_count_without_beacon_on_line(2000000, s, b)
print(len(blocked)-1)