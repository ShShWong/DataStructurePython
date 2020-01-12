class Algorithms():
    def __init__(self):
        super().__init__()


    def swap(self,lyst,i,j):
        temp = lyst[i]
        lyst[i] = lyst[j]
        lyst[j] = temp
        return lyst

    def selectionSort(self,lyst):
        i = 0
        while i < len(lyst)-1:
            j = i + 1
            while j < len(lyst):
                if lyst[j] < lyst[i]:
                    swap(lyst,i,j)
                j += 1
            i += 1
        return lyst

    def bubbleSort(self,lyst):
        n = len(lyst)
        while n > 1:
            i = 1
            while i < n:
                if lyst[i] < lyst[i - 1]:
                    swap(lyst,i,i-1)
                i += 1
            n -= 1
        return lyst

    def quickSort(self,lyst):
        if len(lyst) < 2:
            return lyst
        pivot = lyst[len(lyst) // 2]
        left = [x for x in lyst if x < pivot]
        
        right = [x for x in lyst if x > pivot]
        middle = [x for x in lyst if x == pivot]

        
        return quickSort(left)+middle+quickSort(right)
