class Counter(object):
    instance = 0

    def __init__(self):
        Counter.instance += 1
        self.reset()
    
    def reset(self):
        self._value = 0
    
    def increment(self,amount = 1):
        self._value += amount

    def decrement(self,amount = 1):
        self._value -= amount

    def getValue(self):
        return self._value
    
    def __str__(self):
        return str(self._value)

    def __eq__(self,other):
        return self._value == other._value

# 每创建一个新的Counter对象，类变量instance就+1，写在类的构造方法中。   
c1 = Counter()
print(Counter.instance)
c2 = Counter()
print(Counter.instance)
print(c1.getValue())
c1.increment()
print(c1.getValue())
c3 = Counter()
print(Counter.instance)
print(c1.__eq__(c2))
print(c1)
