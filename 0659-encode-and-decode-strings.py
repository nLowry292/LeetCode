
# Online Python - IDE, Editor, Compiler, Interpreter

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        n = len(strs)
        if n == 1:
           return strs[0]
        res = ""
        for i in range(n-1):
            res = res + strs[i] + "#"
        return res + strs[n]

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        currentWord = ""
        for char in str:
            if char != "#":
                currentWord = currentWord + char
            else:
                res.append(currentWord)
                currentWord = ""
        res.append(currentWord)
        return res
    
