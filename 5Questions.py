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