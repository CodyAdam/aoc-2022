import re

lines = open("input.txt").read().splitlines()
blueprints = []
for line in lines:
    regexp = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
    index, ore, clay, obsi1, obsi2, geode1, geode2 = map(
        int,
        re.findall(regexp, line)[0])
    blueprints.append((index, ore, clay, obsi1, obsi2, geode1, geode2))

MAX_TIME = 32


class State:

    def __init__(self, blueprint, state=None) -> None:
        if state == None:
            self.history = []
            self.blueprint = blueprint
            self.time = 0
            self.r_ore = 1
            self.r_clay = 0
            self.r_obsidian = 0
            self.r_geode = 0
            self.ore = 0
            self.clay = 0
            self.obsidian = 0
            self.geode = 0
        else:
            self.history = state.history.copy()
            self.blueprint = blueprint
            self.time = state.time
            self.r_ore = state.r_ore
            self.r_clay = state.r_clay
            self.r_obsidian = state.r_obsidian
            self.r_geode = state.r_geode
            self.ore = state.ore
            self.clay = state.clay
            self.obsidian = state.obsidian
            self.geode = state.geode

    def collect(self):
        self.ore += self.r_ore
        self.clay += self.r_clay
        self.obsidian += self.r_obsidian
        self.geode += self.r_geode

    def make_ore(self):
        self.ore -= self.blueprint[1]
        self.r_ore += 1
        self.history.append(f"ore (-{self.blueprint[1]})")

    def make_clay(self):
        self.ore -= self.blueprint[2]
        self.r_clay += 1
        self.history.append(f"clay (-{self.blueprint[2]})")

    def make_obsidian(self):
        self.ore -= self.blueprint[3]
        self.clay -= self.blueprint[4]
        self.r_obsidian += 1
        self.history.append(
            f"obsidian (-{self.blueprint[3]}/{self.blueprint[4]})")

    def make_geode(self):
        self.ore -= self.blueprint[5]
        self.obsidian -= self.blueprint[6]
        self.r_geode += 1
        self.history.append(
            f"geode (-{self.blueprint[5]}/{self.blueprint[6]})")

    def wait(self):
        self.history.append("wait")

    def get_next(self):
        global maxi
        _, ore, clay, obsi1, obsi2, geode1, geode2 = self.blueprint
        if self.time == MAX_TIME:
            if self.geode > maxi:
                maxi = self.geode
                print("  ", maxi)
                # for index, history in enumerate(self.history):
                #     print(index, history)
                # print("-----------------")
            return []
        news = []

        if self.ore >= geode1 and self.obsidian >= geode2:
            geode_maker = State(self.blueprint, self)
            geode_maker.collect()
            geode_maker.time += 1
            geode_maker.make_geode()
            news.append(geode_maker)
        elif self.ore >= obsi1 and self.clay >= obsi2 and (geode2 >
                                                           self.r_obsidian):
            obsidian_maker = State(self.blueprint, self)
            obsidian_maker.collect()
            obsidian_maker.time += 1
            obsidian_maker.make_obsidian()
            news.append(obsidian_maker)
        else:
            if self.ore >= ore and (clay > self.r_ore or ore > self.r_ore or
                                    obsi1 > self.r_ore or geode1 > self.r_ore):
                ore_maker = State(self.blueprint, self)
                ore_maker.collect()
                ore_maker.time += 1
                ore_maker.make_ore()
                news.append(ore_maker)
            else:
                waiter = State(self.blueprint, self)
                waiter.collect()
                waiter.time += 1
                waiter.wait()
                news.append(waiter)
            if self.ore >= clay and (obsi2 > self.r_clay):
                clay_maker = State(self.blueprint, self)
                clay_maker.collect()
                clay_maker.time += 1
                clay_maker.make_clay()
                news.append(clay_maker)

        return news

    def __str__(self) -> str:
        return f"T: {self.time}, {self.ore}({self.r_ore}), {self.clay}({self.r_clay}), {self.obsidian}({self.r_obsidian}), {self.geode}({self.r_geode})"

    def __repr__(self) -> str:
        return str(self)


s = 1
for b in blueprints[:3]:

    maxi = 0
    print("Blueprint", b[0], ":")
    state = State(b)
    states = state.get_next()
    while len(states):
        state = states.pop()
        # print(state.time)
        states.extend(state.get_next())
    s *= maxi
print(s)