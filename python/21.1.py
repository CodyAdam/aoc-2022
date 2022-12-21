import re


def calculate(val1, op, val2):
    if op == "+":
        return val1 + val2
    elif op == '*':
        return val1 * val2
    elif op == "-":
        return val1 - val2
    elif op == "/":
        return int(val1 / val2)

    print("Error ope not found : ", val1, op, val2)
    exit()


values = {}
operations = {}
for line in open("input.txt").read().splitlines():
    var, value = re.findall(r"(\w+): (.*)", line)[0]
    value = value.split()
    if len(value) == 1:
        values[var] = int(value[0])
    else:
        operations[var] = tuple(value)

changed = True
while changed:
    changed = False
    new_values = {}
    for var in operations:
        left, op, right = operations[var]
        if left in values and right in values:
            values[var] = calculate(values[left], op, values[right])
            changed = True
        else:
            new_values[var] = operations[var]
    operations = new_values

print(values["root"])