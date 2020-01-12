import numpy as np 
def calThePi(n=8):
    if  n == 0:
        return 1
    return  calThePi(n-1) + np.power(-1,n)*(1.0/(2*n+1))

print(calThePi(100)*4)