file = open("input.txt").read()


def check_signal():
    global signal, cycle
    cycle += 1
    if (20 + cycle) % 40 == 0:
        signal += x * cycle


x = 1
signal = 0
cycle = 0

for line in file.splitlines():
    command = line.strip().split()
    if len(command) == 2:
        command, value = command
    else:
        command = command[0]

    # Noop
    if command == "noop":
        check_signal()

    # AddX
    if command == "addx":
        check_signal()
        check_signal()
        x += int(value)

print(signal)
