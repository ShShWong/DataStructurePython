from node import Node


class Tester(object):
    def __init__(self):
        super().__init__()
        
    def length(self,head):
        result = 0
        while head != None:
            if head.data != None:
                result += 1
            head = head.next
        return result

    def insert(self,index,data,head):
        count = 0
        insertNode = Node(data,next=None)
        while head != None:
            count += 1
            if count == index+1:
                insertNode.next = head.next
                insertNode.data = data
                head.next == insertNode
            return head
                


head = None
for count in range(5):
    head = Node(count,head)

# while head != None:
#     print(head.data)
#     head = head.next

test = Tester()
print(test.length(head))
test.insert(1,10,head)
while head != None:
    print(head.data)
    head = head.next

