def fib(dic):
    key = dic.keys
    value = dic.values
    if key < 3:
        return 1
    else:
        return fib(n-1)+fib(n-2)

dic = {'key':'value'}
print(dic.keys())