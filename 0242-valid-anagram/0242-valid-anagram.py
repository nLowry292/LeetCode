class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        for char in t:
            chars[char] = chars.get(char, 0) - 1
        for char in chars:
            if chars[char] != 0:
                return False
        return True