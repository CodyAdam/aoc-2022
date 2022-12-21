import re
from sympy.solvers import solve
from sympy import Symbol

values = {}
for line in open("input.txt").read().splitlines():
    var, value = re.findall(r"(\w+): (.*)", line)[0]
    value = value.split()
    if len(value) == 1:
        values[var] = int(value[0])
    else:
        if var == "root":
            values[var] = (value[0], "-", value[2])
        else:
            values[var] = tuple(value)
del values["humn"]


def get(var):
    if var in values:
        val = values[var]
        if isinstance(val, int):
            return val
        else:
            left, op, right = val
            return (get(left), op, get(right))
    else:
        return var


print(get("root"))

humn = Symbol("humn")
res = solve((((4 + (2 * (humn - 3))) / 4) - ((32 - 2) * 5)), humn)
print(res)
