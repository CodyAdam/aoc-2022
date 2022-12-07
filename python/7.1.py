from collections import defaultdict

file = open("input.txt").read()

group_of_commands = [
    x.strip() for x in file.split("$") if (len(x) > 1 and x[0] != "")
]

sizes = []
tree = defaultdict(list)
path = "/"
for group in group_of_commands:
    commands = group.split("\n")
    first = commands[0]
    if first[0:2] == "cd":
        target = first.split(" ")[1]
        if target[0] == ".":
            path = "/".join(path.split("/")[:-2]) + "/"
        elif target[0] != "/":
            path = path + target + "/"
        else:
            path = target
    if first[0:2] == "ls":
        files = commands[1:]
        for f in files:
            size, name = f.split(" ")
            if size == "dir":
                tree[path].append(path + name + "/")
            else:
                size = int(size)
                tree[path].append(size)


def getSize(path):
    size = 0
    for x in tree[path]:
        if type(x) == int:
            size += x
        else:
            size += getSize(x)
    return size


summ = 0
for key, value in tree.items():
    size = getSize(key)
    print("{:>42} {:>12}".format(key, size))
    if size <= 100000:
        summ += size

print(summ)
