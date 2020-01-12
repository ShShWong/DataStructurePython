def displayRange(lower,upper):
    if lower <= upper:
        print(lower,end=" ")
        displayRange(lower+1,upper)

# displayRange(1,10)

def factorical(n):
    if(n==1):
        return 1
    return n*factorical(n-1)
print(factorical(5))
        