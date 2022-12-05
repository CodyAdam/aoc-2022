from collections import defaultdict

with open("input.txt") as file:
    file = file.read()

# PARSE INPUT
board, commands = file.split("\n\n")
board = board.replace("[", " ").replace("]", " ").splitlines()[:-1]
commands = [line.strip() for line in commands.splitlines()]
stack = defaultdict(lambda: [])
for index in range(len(board) - 1, 0 - 1, -1):
    line = board[index][1:] + " "

    for i in range(0, len(line), 4):
        if line[i] == " ": continue
        else: stack[i // 4].append(line[i])

print(stack)

# EXECUTE COMMANDS
for command in commands:
    command = command.replace("move ", "").replace(" from ",
                                                   " ").replace(" to ", " ")
    count, from_, to = map(int, command.split())
    to_add = []
    for i in range(count):
        to_add.append(stack[from_ - 1].pop())
    to_add.reverse()
    for x in to_add:
        stack[to - 1].append(x)

for i in range(len(stack)):
    print(stack[i][-1], end="")
print()
