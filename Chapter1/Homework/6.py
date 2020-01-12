import pickle

lyst = ["Bob",100,10]
fileObj = open("Salary.dat","wb")
for item in lyst:
    pickle.dump(item,fileObj)
fileObj.close()

lyst = list()
fileObj = open("Salary.dat","rb")
while True:
    try:
        item = pickle.load(fileObj)
        lyst.append(item)
    except EOFError:
        fileObj.close()
        break
print(lyst)