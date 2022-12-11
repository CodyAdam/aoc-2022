from collections import defaultdict
from functools import reduce

file = open("input.txt").read()

# PARSE INPUT
monkey_items = defaultdict(list)
monkey_ope = {}
monkey_test = {}
monkeys = [m.splitlines() for m in file.split("\n\n")]
order = []
for monkey in monkeys:
    [identifier, items, ope, *test] = monkey
    index = identifier.split()[1][:-1]
    order.append(index)

    items = [int(x) for x in items.split(":")[1].strip().split(', ')]
    monkey_items[index] = items

    ope = ope.split(" = ")[1].split()
    monkey_ope[index] = ope

    test_divisible_by = int(test[0].split("by ")[1])
    if_true = test[1].split("monkey ")[1]
    if_false = test[2].split("monkey ")[1]
    monkey_test[index] = (test_divisible_by, if_true, if_false)

# SOLVE


def get_new_stress(stress, ope):
    left, op, right = ope
    if right == "old":
        right = stress
    else:
        right = int(right)
    if left == "old":
        left = stress
    else:
        left = int(left)
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return left // right
    else:
        raise ValueError("Unknown operator", op)


def is_divisible_by(stress, test_divisible_by):
    return stress % test_divisible_by == 0


monkey_inspections_count = defaultdict(int)
for _ in range(20):
    for monkey_index in order:
        items = monkey_items[monkey_index]
        ope = monkey_ope[monkey_index]
        test_divisible_by, if_true, if_false = monkey_test[monkey_index]

        items_count = len(items)
        for item in items:
            monkey_inspections_count[monkey_index] += 1
            item = get_new_stress(item, ope)
            item = item // 3
            if is_divisible_by(item, test_divisible_by):
                monkey_items[if_true].append(item)
            else:
                monkey_items[if_false].append(item)
        monkey_items[monkey_index] = monkey_items[monkey_index][items_count:]

best_monkey = sorted(monkey_inspections_count.values(), reverse=True)[:2]
print(reduce(lambda x, y: x * y, best_monkey))
