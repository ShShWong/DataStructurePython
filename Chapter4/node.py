class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    
    def nextData(self):
        return self.next.data
    

# node1 = None
# node2 = Node("A",None)
# node3 = Node("B",node2)
# node1 = Node("C")
# node1.next = node3
# print(node1.nextData())

