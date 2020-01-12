from grid import Grid
from arrays import Array

class Grid3D(object):
    def __init__(self,rows,cols,depths,fillValue=None):
        self._rows   = rows
        self._cols   = cols
        self._depths = depths
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Grid(cols,depths)
    
    def getHeight(self):
        return len(self._data)
    
    def getWidth(self):
        return len(self._data[0])
    
    def getDepth(self):
        return len(self._data[1])

    def __getitem__(self,index):
        return self._data[index]

    def __str__(self):
        result = ""
        for row in range(self._rows):
            for col in range(self._cols):
                for depth in range(self._depths):
                    result += str(self._data[row][col][depth])+' '
                result += '\n'
        return result
    
g3 = Grid3D(2,3,1,1)
print(g3.getDepth)
print(g3.getWidth)
print(g3.getHeight)

