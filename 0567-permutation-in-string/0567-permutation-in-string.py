import numpy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = numpy.array([0]*26)
        s2count = numpy.array([0]*26)
        for char in s1:
            s1count[ord(char)-ord('a')] += 1
        for i in range(len(s1)):
            s2count[ord(s2[i])-ord('a')] += 1
        for j in range(len(s2)-len(s1)+1):
            if numpy.array_equal(s1count,s2count):
                return True
            if j == len(s2)-len(s1):
                return False
            s2count[ord(s2[j])-ord('a')] -= 1
            s2count[ord(s2[j+len(s1)])-ord('a')] += 1