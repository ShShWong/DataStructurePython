from node import Node
from arrays import Array

outArr = Array(5,1)
for i in range(len(outArr)):
    outArr[i] = i + 1

head = None

for count in range(len(outArr)):
    head = Node(outArr[count],head)

while head != None:
    print(head.data)
    head = head.next