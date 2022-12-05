lines = open("input.txt").readlines()

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def letter_value(l):
    if l in lowercase:
        return -ord('a') + ord(l) + 1
    elif l in uppercase:
        return ord(l) - ord('A') + 27


s = 0
print(letter_value('z'))
for line in lines:
    left = set(line[0:len(line) // 2])
    right = set(line[len(line) // 2:])

    inter  = left & right
    for char in inter:
        s += letter_value(char)

print(s)