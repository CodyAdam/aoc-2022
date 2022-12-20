class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        s = ""
        n = self
        while True:
            s += str(n.data) + " "
            n = n.next
            if n == self:
                break
        return s

    def move(self, n) -> None:
        if n == 0:
            return
        cursor = self
        self.prev.next = self.next
        self.next.prev = self.prev
        if n < 0:
            cursor = cursor.prev
        for _ in range(abs(n)):
            if n > 0:
                cursor = cursor.next
            else:
                cursor = cursor.prev

        self.next = cursor.next
        self.prev = cursor
        cursor.next.prev = self
        cursor.next = self

    def __repr__(self) -> str:
        return self.__str__()


lines = open("input.txt").read().splitlines()
head = None
for line in lines:
    x = int(line)
    if head is None:
        head = Node(x)
        head.next = head
        head.prev = head
    else:
        new = Node(x)
        new.next = head
        new.prev = head.prev
        head.prev.next = new
        head.prev = new

arr = [head]
current = head
while current.next != head:
    current = current.next
    arr.append(current)
    if current.data == 0:
        zero = current

for node in arr:
    node.move(node.data)

current = zero
s = 0
for i in range(1, 3001):
    current = current.next
    if i in [1000, 2000, 3000]:
        s += current.data
        print(i, current.data)
print(s)