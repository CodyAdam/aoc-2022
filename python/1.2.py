try:
    with open("input.txt") as file:
        file = file.read()
except:
    print("File not found")
    exit()

lines = [line.strip() for line in file.splitlines()]


arr = []
current = []
for line in lines: 
    if line == "":
        arr.append(current)
        current = []
    else:
        current.append(int(line))
arr.append(current)
current = []

arr = [sum(x) for x in arr]
print(arr)
arr.sort()
print(sum(arr[-3:]))