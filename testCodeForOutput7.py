#    test6.py

from linkedlist import *

mylist = LinkedList()
mylist.append("cat")
mylist.append("elephant")
mylist.append("lion")
mylist.append("lizard")

print("original list\n-----------------------------")
mylist.print()

mylist[0] = "ant"
mylist[3] = "alligator"

print("changed list\n-----------------------------")

mylist.print()

print("\n\nNow try to do outside the bounds...")

try:
	mylist[10] = "dog"
except Exception as e:
	print(e)

