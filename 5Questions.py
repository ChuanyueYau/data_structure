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

