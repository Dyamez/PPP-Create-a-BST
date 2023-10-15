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
        if new_node.data > current_node.data:
            if current_node.right is None:
                current_node.right = new_node
                self.contents.append(new_node.data)
                return
            else:
                self.add_node(current_node.right, new_node)
        else:
            if current_node.left is None:
                current_node.left = new_node
                self.contents.append(new_node.data)
                return
            else:
                self.add_node(current_node.left, new_node)

    def remove(self, int_or_node):
        node_type = type(int_or_node)

        if node_type is not int and node_type is not BSTNode:
            raise ValueError("You must only ints or BST nodes allowed")
        
        node_value = None
        
        if node_type is BSTNode:
            node_value = int_or_node.data
        else:
            node_value = int_or_node

        if node_value not in self.contents:
            raise ValueError(f"The value {node_value} was not found")
        
        self.remove_node(self.root, node_value)

    def remove_node(self, curr_node, remove_value, prev_node=None): 
        if remove_value is curr_node.data:
            if curr_node.right is None and curr_node.left is None:
                if curr_node is prev_node.right:
                    prev_node.right = None
                else:
                    prev_node.left = None
                self.contents.remove(remove_value)
            elif curr_node.right is None and curr_node.left is not None:
                if curr_node is prev_node.right:
                    prev_node.right = curr_node.left
                else:
                    prev_node.left = curr_node.left
                self.contents.remove(remove_value)
            elif curr_node.left is None and curr_node.right is not None:
                if curr_node is prev_node.left:
                    prev_node.left = curr_node.right
                else:
                    prev_node.right = curr_node.right
                self.contents.remove(remove_value)
            else:
                self.nodes = []
                self.traverse_tree(curr_node)
                self.nodes.remove(remove_value)
                self.contents.remove(remove_value)

                if curr_node is prev_node.right:
                    prev_node.right = None
                else:
                    prev_node.left = None

                for node_value in self.nodes:
                    self.add(node_value)
        elif remove_value > curr_node.data:
            self.remove_node(curr_node.right, remove_value, prev_node=curr_node)
        elif remove_value < curr_node.data:
            self.remove_node(curr_node.left, remove_value, prev_node=curr_node)



                
        
    def traverse_tree(self, node):
        if node is not None:
            self.traverse_tree(node.right)
            self.nodes.append(node.data)
            self.traverse_tree(node.left)

            
            
       


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

node_8 = BSTNode(8)
node_3 = BSTNode(3)
node_10 = BSTNode(10)
node_1 = BSTNode(1)
node_6 = BSTNode(6)
node_14 = BSTNode(14)
node_4 = BSTNode(4)
node_7 = BSTNode(7)
node_13 = BSTNode(13)


bst_0 = BST()
bst_0.add(node_8)
bst_0.add(node_3)
bst_0.add(node_10)
bst_0.add(node_1)
bst_0.add(node_6)
bst_0.add(node_14)
bst_0.add(node_4)
bst_0.add(node_7)
bst_0.add(node_13)

print(bst_0)

print('################################')

