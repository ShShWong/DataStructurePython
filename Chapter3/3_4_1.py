def swap(lyst,i,j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    return lyst

def selectionSort(lyst):
    i = 0
    while i < len(lyst)-1:
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[i]:
                swap(lyst,i,j)
            j += 1
        i += 1
    return lyst

lyst = [5,4,3,2,1,0]
print(selectionSort(lyst))
