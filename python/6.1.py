from collections import defaultdict

with open("input.txt") as file:
    file = file.read()

lines = file.splitlines()
for line in lines:

    done = False
    for i in range(len(line) - 14):
        if done:
            break
        if len(line[i:i + 14]) == len(set(line[i:i + 14])):
            done = True
            break

    print(line[i:i + 14], i+14)
