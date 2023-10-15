#Part 1: Create a BSTNode class
class BSTNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return BSTNode.__str__(self)
    
node_0 = BSTNode(1)
print(node_0)

node_1 = BSTNode(420, left=node_0)
print(node_1)

node_2 = BSTNode()
print(node_2)
node_2.data = 8088
print(node_2)

print('####################################################')

#Part 2: Create a BST class
  #Part 3: Add functionality to your BST class

class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = [] 

    def __str__(self):
        if self.root is None:
            return "the tree is empty"
        else:
            self.output = ""
            self.print_tree(node=self.root)
            return self.output