from collections import defaultdict
import re

file = open("input.txt").read()

neigh = defaultdict(list)
rateOf = defaultdict(int)
for line in file.splitlines():
    name, rate, connections = re.findall(
        r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)$",
        line)[0]
    rate = int(rate)
    connections = connections.split(", ")
    neigh[name] = connections
    rateOf[name] = rate


def dist(current, node, visited):
    """
    Number of nodes between current and node
    Return None if node is not reachable from current
    """
    if current == node:
        return 0
    visited.add(current)
    mini = None
    for n in neigh[current]:
        if n not in visited:
            d = dist(n, node, visited)
            if d is not None:
                if mini is None or d + 1 < mini:
                    mini = d + 1
    return mini


def bfs(current: str, activated: list, time_left: int):
    if time_left <= 0:
        return 0
    activated.append(current)
    new_activated = []
    value = 0
    for node, rate in rateOf.items():
        if node not in activated and rate > 0:
            d = dist(current, node, set())
            if d is None:
                continue
            time_left_after = (time_left - d - 1)
            if time_left_after > 0:
                bfs_result, other_activated = bfs(node, activated.copy(),
                                                  time_left_after)
                potential_value = (time_left_after * rate) + bfs_result
                if potential_value > value:
                    value = potential_value
                    new_activated = other_activated
    if new_activated:
        return (value, new_activated)
    return (value, activated)


current = "AA"
activated = []
time_left = 30

print(bfs(current, activated, time_left))
