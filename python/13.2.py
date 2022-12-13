import ast
import sys

sys.setrecursionlimit(9000)
file = open("input.txt").read()
#prepend "[[2]] [[6]]"
file = "[[2]]\n[[6]]\n" + file
lines = [ast.literal_eval(line.strip()) for line in file.split("\n") if line.strip() != ""]


# left < right
def left_less_than_right(left, right):
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
            if not left_less_than_right(left[i], right[i]):
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


sorted_arr = []
for i, arr in enumerate(lines):
    if len(sorted_arr) == 0:
        sorted_arr.append(i)
        continue
    for j, sorted_item_index in enumerate(sorted_arr):
        if left_less_than_right(arr, lines[sorted_item_index]):
            sorted_arr.insert(j, i)
            break
        if j == len(sorted_arr) - 1:
            sorted_arr.append(i)
            break
print(sorted_arr)

print((sorted_arr.index(0)+1) * (sorted_arr.index(1)+1))

