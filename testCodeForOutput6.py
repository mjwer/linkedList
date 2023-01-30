#    test6.py

from linkedlist import *

mylist = LinkedList()
mylist.append("cat")
mylist.append("elephant")
mylist.append("lion")
mylist.append("lizard")

mylist.print()

print("item 0 is", mylist.__getitem__(0))

k = 3
print(f"item {k} is", mylist.__getitem__(k))


