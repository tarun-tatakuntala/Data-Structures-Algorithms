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
        self.next = next

class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #print list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #Insertion at the end
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    #Insertion at the start
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = head
            self.tail = tail
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    #Insertion at specific position.
    #To do that we need info about previous node.
    #So we write get() method
    def get(self, index):
        if index < 0 or index >= self.length:   #boundary condition
            return None
        temp = self.head
        for _ in range(index): # _ is used instead of variable when variable is need not to be used.
            temp = temp.next
        return temp
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1

my_linked_list = Linkedlist(1)
my_linked_list.append(2)
my_linked_list.prepend(0)
my_linked_list.insert(1,1)
my_linked_list.print_list()
