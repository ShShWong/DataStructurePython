from arrays import Array
class Grid3d(object):
    def __init__(self,rows,columnsList,depths,fillValue = None):
        self._data = Array(rows)
        for row in range(rows):
            if row == 0:
                self._data[row] = Array(3)
            if row == 1:
                self._data[row] = Array(6)
            if row == 2:
                self._data[row] = Array(8)
            


        