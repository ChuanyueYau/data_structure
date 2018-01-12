"""
Question 1

Given two strings s and t, determine whether some anagram of t is a substring of s.
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.
"""

def permutation(string):
    """
    function to generate all permutations of a string
    """
    if len(string) <= 1:
        yield string
    else:
        for i in range(len(string)):
            for perm in permutation(string[:i] + string[i+1:]):
                yield string[i] + perm
                
def question1(s,t):
    """
    Given two strings s and t, 
    determine whether some anagram of t is a substring of s
    """
    for item in permutation(t):
        
        if item in s:
            return True
        
    return False

# another solution of question 1

def is_anagram(string, t_list):
    """
    function to test whether one string is the anagram of another
    """
    s_list = sorted(list(string))
    return s_list == t_list

def question1_1(s,t):
    
    t_list = sorted(list(t))
    matchLength = len(t)
    
    for i in range(len(s)-matchLength+1):
        substring = s[i:i+matchLength]
        if is_anagram(substring, t_list):
            return True
        
    return False

"""
Question 2

Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.
"""

def question2(a):
    # dictionary stores all potential longest palindromic substring
    substring = {}
    # dictionary stores the index of all unique letter
    letter = {}
    maxLength = 1
    for i,element in enumerate(a):
        if element in letter:
            currentLen = i - letter[element] + 1
            if currentLen >= maxLength:
                maxLength = currentLen
                substring[a[letter[element]:i+1]] = currentLen
        else:
            letter[element] = a.index(element)
    LPS = [sub for sub in substring if substring[sub]==maxLength]
    return LPS


"""
Question 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
For example, the root is a common ancestor of all nodes on the tree, 
but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. 
The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, 
where the index of the list is equal to the integer stored in that node and a 1 represents a child node, 
r is a non-negative integer representing the root, 
and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def build_tree(self, T):
        self.build_tree_helper(self.root, T)
        
    def build_tree_helper(self, start, T):
        """
        helper function to build Binary Search Tree according to tree matrix
        """
        index = start.value
        if sum(T[index]) > 0:
            for i, node in enumerate(T[index]):
                if node == 1:
                    if i < index:
                        start.left = Node(i)
                        self.build_tree_helper(start.left, T)
                    else:
                        start.right = Node(i)
                        self.build_tree_helper(start.right, T)
                        
    def print_tree(self):
        """
        print tree using preorder DFS
        """
        return  self.preorder_print(self.root, '')[:-1]
    
    
    def preorder_print(self, start, traversal):
        """
        helper function of print_tree
        """
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def search(self, find_val):
        """
        search function to find specific value
        """
        return self.BST_search(self.root, find_val)
        
    def BST_search(self, start, find_val):
        """
        helper function of search
        """
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.BST_search(start.right, find_val)
            else:
                return self.BST_search(start.left, find_val)
            
        return False
    
    def LCA(self, n1, n2):
        """
        function to find the least common ancestor between two nodes on the binary search tree
        """
        return self.LCA_helper(self.root, n1, n2)
    
    def LCA_helper(self, start, n1, n2):
        
        if start:
            if start.value < n1 and start.value < n2:
                # if both n1 and n2 are greater than root, then LCA lies in left
                return self.LCA_helper(start.right, n1, n2)
            
            if start.value > n1 and start.value > n2:
                # if both n1 and n2 are smaller than root, then LCA lies in left
                return self.LCA_helper(start.left, n1, n2)
            
            return start.value
        
        return None
    
    
def question4(T, r, n1, n2):
    
    # build tree
    tree = BST(r)
    tree.build_tree(T)
    
    if tree.search(n1) and tree.search(n2):
        return tree.LCA(n1, n2)
    
    else:
        error = "Error: either n1 or n2 is not in the tree!"
        return error
    

            
            
# test case 1: should return 3            
print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4)    

# test case 2: should return 3
print question4([[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], 
                 [1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]], 6, 0, 4)
# test case 3: should return 2
print question4([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 8, 0, 5)
# test case 4: should print error message
print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 2, 4)


"""
Question 5
Find the element in a singly linked list that's m elements from the end. For example, 
if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. 
Return the value of the node at that position.
"""

class Node(object):
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    
    def __init__(self,head=None):
        self.head = head
    
    def append(self,new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
def question5(ll, m):
    length = 1
    current = ll
    while current.next:
        current = current.next
        length += 1
    if length < m:
        return None
    else:
        for i in range(length-m):
            ll = ll.next
        return ll
