def binarySearch(target,sortedLyst):
    left = 0
    right = len(sortedLyst)-1
    while left <= right:
        midpoint = (left+right) // 2
        if target > sortedLyst[midpoint] :
            left = midpoint+1
        if target < sortedLyst[midpoint]:
            right = midpoint-1
        if target == sortedLyst[midpoint]:
            return midpoint

lyst = [1,3,5,7,9]
print(binarySearch(9,lyst))