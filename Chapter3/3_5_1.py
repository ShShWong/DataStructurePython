def quickSort(lyst):
    if len(lyst) < 2:
        return lyst
    pivot = lyst[len(lyst) // 2]
    left = [x for x in lyst if x < pivot]
    
    right = [x for x in lyst if x > pivot]
    middle = [x for x in lyst if x == pivot]

    
    return quickSort(left)+middle+quickSort(right)

lyst = [1,9,5,7,2,3,7,9,0.5]
print(quickSort(lyst))