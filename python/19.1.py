import re

lines = open("input.txt").read().splitlines()
blueprints = []
for line in lines:
    regexp = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
    index, ore, clay, obsi1, obsi2, geode1, geode2 = map(
        int,
        re.findall(regexp, line)[0])
    blueprints.append((index, ore, clay, obsi1, obsi2, geode1, geode2))


def is_possible(n, blueprint):
    index, ore, clay, obsi1, obsi2, geode1, geode2 = blueprint
    


for b in blueprints:
    print("Blueprint", b[0], ":")
    for i in range(1, 5):
        print(i, is_possible(i, b))