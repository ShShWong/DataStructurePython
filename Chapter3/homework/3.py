def pow(num,index):
    if index == 1:
        return num
    return num * pow(num,index-1)

print(pow(2,6))