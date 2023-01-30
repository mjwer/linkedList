# Matthew Werner
# CSC 512
# LinkedLists Mini Project

class LinkedList:
        class Node:
                def __init__(self, payload):
                        self.payload = payload
                        self.next = None

        def __init__(self):
                self.head = None
                self.tail = None

        def append(self, newdata):
                '''Adds a new node to the end of the list.'''
                assert type(newdata) is str, 'Newdata must be a string.'
                newnode = LinkedList.Node(newdata)
                if self.empty():
                        self.head = newnode
                        self.tail = newnode
                else:
                        self.tail.next = newnode
                        self.tail = newnode

        def empty(self):
                ''' Returns an empty list.'''
                return self.head is None and self.tail is None

        def print(self):
                '''Prints out the entire list.'''
                runner = self.head
                while runner is not None:
                        print(str(runner.payload))
                        runner = runner.next 

        #------------- from this point on they write -----------------

        def length(self):
                runner = self.head
                count = 0
                while runner != None:
                        count += 1
                        runner = runner.next
                return count

        def __len__(self):
                return self.length()

        def __getitem__(self, index):
                assert type(index) is int, 'Index must be an integer.'
                runner = self.head
                count = 0
                while runner != None:
                        if count == index:
                                return runner.payload
                        else:
                                count += 1
                                runner = runner.next
                raise IndexError(str(index) + ' is out of bounds.  There are only ' + str(count)+ ' items in this list.')

        def __setitem__(self, index, newvalue):
                assert type(index) is int, 'Index must be an integer.'
                assert type(newvalue) is str, 'newvalue must be a string.'
                count =0
                runner = self.head
                while count < index and runner is not None:
                        count += 1
                        runner = runner.next
                if count == index:
                        runner.payload = newvalue
                else:
                        raise IndexError(f'ERROR! Out of bounds, index {index} is above the length of {count}')	
