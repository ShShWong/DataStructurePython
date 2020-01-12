def indexOfMin(lyst):
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

lyst = [5,2,9,4,1,-2,12,100]
print(indexOfMin(lyst))