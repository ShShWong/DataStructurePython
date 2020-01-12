class Book():
    def __init__(self,title,author,borrower,borrowingList):
        self.title = title
        self.author = author
        self.borrower = borrower
        self.borrowingList = borrowingList
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author

    def getBorrower(self):
        return self.borrower

    def getBorrowingList(self):
        return self.borrowingList

class Patron():

    def __init__(self):
        self.max_borrow = 3
        self._borrowNumber = 0
        self._borrowList = []

    def borrow(self,Book):
        self._borrowNumber += 1
        if(self._borrowNumber <= self.max_borrow):
            self._borrowList.append(Book.getTitle())
        else:
            print("Cannot borrow more than three books")
    
    def getBorrowList(self):
        return self._borrowList
    
    def getBorrowNumber(self):
        return self._borrowNumber
    
b1 = Book("PythonCookBook","Tom","Me","smith")
b2 = Book("JavaCookBook","Tom","Me","smith")
b3 = Book("C++CookBook","Tom","Me","Smith")
b4 = Book("OCCookBook","Tom","Me","Smith")
p1 = Patron()
p1.borrow(b1)
p1.borrow(b2)
# print(p1.getBorrowList())
# p1.borrow(b3)

p1.borrow(b4)
print(p1.getBorrowList())




