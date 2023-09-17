"""
Insertion operation has 3 versions.
1. Insertion at the front of linked list(Prepend)
2. Insertion at the end of linked list(Append)
3. Insertion at the specific position
For 3rd operation we need the index of element at which it needs to be inserted.

"""
# Node class for new nodes. Every time we call theis node class, new node will be created.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # calling the Node class to create the node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        if temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


my_ll = LinkedList(1)
my_ll.append(2)
my_ll.print_list()
