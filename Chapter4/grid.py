from arrays import Array
class Grid(object):
    def __init__(self,rows,columns,fillValue =None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns,fillValue)
    
    def getHeight(self):
        return len(self._data)
    
    def getWidth(self):
        return len(self._data[0])
    
    def __getitem__(self,index):
        return self._data[index]
    
    def __str__(self):
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col])+' '
            result += '\n'
        return result


g = Grid(4,5,1)
print(g)
    