#    test1.py

from linkedlist import *

mylist = LinkedList()
mylist.append("cat")
mylist.append("elephant")
mylist.append("lion")
mylist.append("lizard")

print("The list is\n-----------------")
mylist.print()
print()

print("length is",mylist.length())

print("length is", len(mylist))

