class Array(object):

    def __init__(self,capacity,fillValue = None):
        super().__init__()
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)
    
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)
    
    def __iter__(self):
        return iter(self._items)

    def __getitem__(self,index):
        return self._items[index]

    def __setitem__(self,index,newItem):
        self._items[index] = newItem
    
    def get(self):
        return self._items

# a = Array(6,1)
# print(a[2])
# for i in range(len(a)):
#     a[i] = i+1

# print(a)






