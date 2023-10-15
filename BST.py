# Part 1: Create a BSTNode class
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
        
    def __repr__(self):
        return BST.__str__(self)
        
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            self.output += ' ' * 4 * level + ' -> ' + str(node.data) + '\n'
            self.print_tree(node.left, level + 1)

    def add(self, int_or_node):
        node_type = type(int_or_node)
        if node_type is not int and node_type is not  BSTNode:
            raise ValueError("You can only add nodes or ints")
        
        if node_type is int:
            int_or_node = BSTNode(int_or_node)

        if int_or_node.data in self.contents:
            return
        
        if self.root is None:
            self.root = int_or_node
            self.contents.append(self.root.data)
            return
        
        self.add_node(self.root, int_or_node)
        
    def add_node(self, current_node, new_node):
          pass

bst = BST()
print(bst)

bst.root = node_0
print(bst)

bst.right = node_2
print(bst)

node_3 = BSTNode(9099)
node_0.left = node_3
print(bst)

print('#######################################################')
