#    test4.py

from linkedlist import *

mylist = LinkedList()
mylist.append("cat")
mylist.append("elephant")
mylist.append("lion")
mylist.append("lizard")

try:
	x = mylist[5]
	print("The 5th thing is " + x)
except Exception as e:
	print("Error!")
	print(e)



