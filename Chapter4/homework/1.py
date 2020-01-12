# import arrays.Array
from arrays import Array

class ArrayList(Array):
    def __init__(self, capacity, fillValue=None):
        super().__init__(capacity, fillValue=fillValue)
        self._oricapacity = capacity
        self._capacity    = capacity
        self._data        = super(ArrayList,self).get()
        self._logicalSize = 0
        if fillValue == None:
            self._logicalSize = self._capacity
    
    def get(self):
        return self._data
    
    def size(self):
        return self._logicalSize

    def __getitem__(self,index):
        if 0 <= index < self.size():
            return super(ArrayList,self).__getitem__(index)
        else:
            raise Exception("Index Error:out of range")

    def __setitem__(self,index,newItem):
        if 0 <= index < self.size():
            return super(ArrayList,self).__setitem__(index,newItem)
        else:
            raise Exception("Index Error:out of range")
    
a = ArrayList(5,1)

print(a.size())
