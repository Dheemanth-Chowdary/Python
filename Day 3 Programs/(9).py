class Solution:
    def isMatch(self, s, p):
        import re
        pattern = re.compile("^" + p + "$")
        if pattern.search(s) is None:
            return False
        else:
            return True
S=input("enter the word") 
P=input("enter the word")
