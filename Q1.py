from collections import Counter
class Q1:

    #To store a list of items
    def __init__(self, y):
        self.x = y

    #insert new items to the list
    def insertVal(self, pos, value):
        self.x.insert(pos, value)

    #A method to return all unique items from the list
    def getUnique(self):
        return set(self.x)

    #A method to return all items and their frequency
    def itemFreq(self):
        return Counter(self.x)

    #append new items to the list
    def appendVal(self, value):
        self.x.append(value)

    def printer(self):
        print(self.x)

'''
******** Testing for the above code *********
ReadMe file is there for input specifications
'''
#read data from input file
f = open('input1.txt', 'r')
data = f.read()
inList = data.splitlines()
initialList = []
for i in range(int(inList[0])):
    initialList.append(inList[i + 1])
myList = Q1(initialList)

'''
unique : unique items from the list
frequency : all items and their frequency
insert :  insert new items to the list
append: append new items to the list
print: to print the list
'''
for j in inList[int(inList[0]) + 1 : len(inList)]:
    operation = j.split()
    if operation[0] == "insert":
        myList.insertVal(int(operation[1]), operation[2])
    if operation[0] == "append":
        myList.appendVal(operation[1])
    if operation[0] == "unique":
        myList.getUnique()
    if operation[0] == "frequency":
        myList.itemFreq()
    if operation[0] == "print":
        myList.printer()

print(myList.itemFreq())
print(myList.getUnique())