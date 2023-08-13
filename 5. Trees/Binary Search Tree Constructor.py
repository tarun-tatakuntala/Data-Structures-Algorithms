#Our aim is to create a binary search tree constructor which has root as None

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

my_binary_tree = BinarySearchTree()
print(my_binary_tree.root)