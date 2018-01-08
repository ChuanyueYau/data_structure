class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, '')[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()



"""
BST: Binary Search Tree
"""

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.BST_insert(self.root, new_val)

    def search(self, find_val):
        return self.BST_search(self.root, find_val)
        
    def print_tree(self):
        return  self.preorder_print(self.root, '')[:-1]
        
    def BST_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.BST_search(start.right, find_val)
            else:
                return self.BST_search(start.left, find_val)
        return False
        
    def BST_insert(self, start, new_val):
        if start.value < new_val:
            if start.right:
                self.BST_insert(start.right, new_val)
            else:
                start.right = Node(new_val)
        else:
            if start.left:
                self.BST_insert(start.left, new_val)
            else:
                start.left = Node(new_val)
            
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
# Set up tree
bst_tree = BST(4)

# Insert elements
bst_tree.insert(2)
bst_tree.insert(1)
bst_tree.insert(3)
bst_tree.insert(5)

# Check Insert construct correctly
# Should be 4-2-1-3-5
print bst_tree.print_tree()

# Check search
# Should be True
print bst_tree.search(5)
# Should be False
print bst_tree.search(6)
