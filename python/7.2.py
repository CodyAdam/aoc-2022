from collections import defaultdict

file = open("input.txt").read()

group_of_commands = [
    x.strip() for x in file.split("$") if (len(x) > 1 and x[0] != "")
]

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


space_needed = 30000000 - (70000000 - getSize("/"))
deletable = []
for key, value in tree.items():
    size = getSize(key)
    print("{:>40} {:>12}".format(key, size))
    if size >= space_needed:
        deletable.append(key)

key = min(deletable, key=lambda x: getSize(x))
print(getSize(key))
