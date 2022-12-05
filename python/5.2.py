from collections import defaultdict

with open("input.txt") as file:
    file = file.read()

board, commands = file.split("\n\n")
board = board.replace("[", " ").replace("]", " ").splitlines()[:-1]
commands = [line.strip() for line in commands.splitlines()]
stack = defaultdict(lambda: [])
for index in range(len(board) - 1, 0 - 1, -1):
    line = board[index][1:] + " "
    print("---- ", index, "'" + line + "'")

    for i in range(0, len(line), 4):
        print(i // 4, line[i])
        if line[i] == " ": continue
        else: stack[i // 4].append(line[i])

print(stack)

for command in commands:
    count, from_, to = command.replace("move ",
                                       "").replace(" from ",
                                                   " ").replace(" to ",
                                                                " ").split()
    count, from_, to = int(count), int(from_) - 1, int(to) - 1
    print(count, from_, to)

    to_add = []
    for i in range(count):
        to_add.append(stack[from_].pop())
    to_add.reverse()
    for x in to_add:
        stack[to].append(x)

for i in range(len(stack)):
    print(stack[i][-1], end="")

print()
