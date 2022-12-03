lines = open("input.txt").readlines()

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def letter_value(l):
    if l in lowercase:
        return -ord('a') + ord(l) + 1
    elif l in uppercase:
        return ord(l) - ord('A') + 27
    else: 
        print("Error: " + l)
        return 0


s = 0
i = 0
arr = []
for line in lines:
    arr.append(set(line.strip()))

    if i == 2:
        print(arr)
        inter = arr[0] & arr[1] & arr[2]
        print(inter)
        for char in inter:
            s += letter_value(char)
        i = -1
        arr = []
    i += 1

print(s)