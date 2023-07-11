class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        split_s = list(s)
        split_t = list(t)
        split_s.sort()
        split_t.sort()
        return split_s == split_t