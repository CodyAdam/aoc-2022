from collections import defaultdict

with open("input.txt") as file:
    file = file.read()

window = 14
for line in file.splitlines():
    for i in range(len(line) - window):
        if window == len(set(line[i:i + window])):
            break

    print(line[i:i + window], i + window)
