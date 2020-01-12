from algorithms import Algorithms
import random
import time
# ALGORITHMS = ['quick']
# def test(nameOfAlgorithm='selectionSort',sizeOfProblem = 10):

class Profiler():
    def __init__(self,sizeOfProblem,algorithm='selectionSort'):
        super().__init__()
        self.algorithm = algorithm
        self.sizeOfProblem = sizeOfProblem
    
    def generateList(self):
        self._lyst = [] 
        for i in range(self.sizeOfProblem):
            self._lyst.append(random.randint(1,100))
    
    def test(self):
        self.generateList()
        start = time.time()
        al = Algorithms()
        al.selectionSort(self._lyst)
        end = time.time()
        print("Problem Size: ",self.sizeOfProblem)
        print("total time: ",end-start)
            