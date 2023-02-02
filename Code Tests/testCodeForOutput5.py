#    test5.py

from linkedlist import *

mylist = LinkedList()
mylist.append("cat")
mylist.append("elephant")
mylist.append("lion")
mylist.append("lizard")

for i in range (0,mylist.length()):
	print(f"{i}. {mylist[i]}")




