def expo(num,exponent):
    left = exponent % 2
    if exponent == 0:
        return 1
    
    if left == 1:
        return num * expo(num,exponent-1)
    elif left == 0:
        return (expo(num,exponent / 2))**2

print(expo(2,3))
print(expo(2,4))





