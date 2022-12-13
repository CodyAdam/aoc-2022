import ast
import sys

sys.setrecursionlimit(9000)
file = open("input.txt").read()
pairs = [line.strip() for line in file.split("\n\n")]


# left < right
def compare_lists(left, right):
    if len(left) == 0 and len(right) == 0:
        return Exception("Both lists are empty")
    if len(left) == 0 and len(right) != 0:
        return True
    if len(left) != 0 and len(right) == 0:
        return False
    for i in range(len(right)):
        if i >= len(left):
            return True
        # left list, right single
        if type(left[i]) == list and type(right[i]) == int:
            right[i] = [right[i]]
        # left single, right list
        if type(left[i]) == int and type(right[i]) == list:
            left[i] = [left[i]]
        # both list
        if type(left[i]) == list and type(right[i]) == list:
            if not compare_lists(left[i], right[i]):
                return False
        # both single integers
        if left[i] < right[i]:
            return True
        elif left[i] > right[i]:
            return False
    # left is longer than right
    if len(left) > len(right):
        return False
    return True


count = 0
for i, pair in enumerate(pairs):
    left, right = [ast.literal_eval(arr) for arr in pair.split("\n")]
    if (compare_lists(left, right)):
        count += i + 1
print(count)