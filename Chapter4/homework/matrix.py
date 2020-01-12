from grid import Grid

class Matrix(Grid):
    def __init__(self, rows, columns, fillValue=None):
        super().__init__(rows, columns, fillValue=fillValue)
        self._data = super(Matrix,self).get()
        self._rows = rows
        self._cols = columns
    
    def __add__(self,obj):
        
        if self._rows == obj._rows and self._cols == obj._cols:
            resMatrix = Grid(self._rows,self._cols)
            for row in range(self._rows):
                for col in range(self._cols):
                    resMatrix[row][col] = self._data[row][col] + obj._data[row][col]
            return resMatrix

    def __sub__(self,obj):
        
        if self._rows == obj._rows and self._cols == obj._cols:
            resMatrix = Grid(self._rows,self._cols)
            for row in range(self._rows):
                for col in range(self._cols):
                    resMatrix[row][col] = self._data[row][col] - obj._data[row][col]
            return resMatrix
        else :
            raise Exception("The matrix dimension don't match")
    
    def __mul__(self,obj):
        temp = 0
        if self._cols == obj._rows:
            resMatrix = Grid(self._rows,obj._cols)
            for row in range(self._rows):
                for col in range(obj._cols):
                    # 从矩阵一拿出来第row行，从矩阵二拿出来第col列 对位相乘再相加即可
                    la = self._data[row]
                    lb = [obj._data[i][col] for i in range(obj._rows)]
                    for i in range(len(la)):
                        resMatrix[row][col] = la[i]*lb[i]

            return resMatrix
        else :
            raise Exception("The matrix dimension don't match")
    

m1 = Matrix(2,1,1)

# print(m1._data[1])
m2 = Matrix(1,4,2)

# print(m1+m2)
# print(m2-m1)
print(m1*m2)