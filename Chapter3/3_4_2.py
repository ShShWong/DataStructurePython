def swap(lyst,i,j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    return lyst

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst,i,i-1)
            i += 1
        n -= 1
    return lyst

lyst = [5,4,3,2,1]
print(bubbleSort(lyst))
                