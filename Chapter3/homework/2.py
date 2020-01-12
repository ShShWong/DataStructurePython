def reverse(lyst):
    n = len(lyst)
    for i in range(n//2):
        temp = lyst[i]
        lyst[i] = lyst[n-1-i]
        lyst[n-1-i] = temp
    return lyst

lyst = [1,2,3,4,5,6]
print(reverse(lyst))

