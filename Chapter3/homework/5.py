def swap(lyst,i,j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    return lyst

def selectionSort(lyst,reverse=False):  
    if reverse:
        i = 0
        while i < len(lyst)-1:
            j = i + 1
            while j < len(lyst):
                if lyst[j] < lyst[i]:
                    swap(lyst,i,j)
                j += 1
            i += 1
    if not reverse:
        i = 0
        while i < len(lyst)-1:
            j = i + 1
            while j < len(lyst):
                if lyst[j] > lyst[i]:
                    swap(lyst,i,j)
                j += 1
            i += 1
    return lyst

lyst = [1,7,8,6,5,3]
print(selectionSort(lyst,reverse = True))
print(selectionSort(lyst))
