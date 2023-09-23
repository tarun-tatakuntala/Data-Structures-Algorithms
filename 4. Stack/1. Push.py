"""
Stack is worked on Last In First Out(LIFO) method. It maily has two operations.
1. Push(Add)
2. Pop(Remove)

The difference between linked list and stack is ll had head and tail, while stack has top and bottom
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1

    def print_list(self):
        temp = self.top
        while(temp):
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

my_stack = Stack(2)
my_stack.push(1)
my_stack.print_list()