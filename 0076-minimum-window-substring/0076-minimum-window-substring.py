class Solution: 
    def minWindow(self, s: str, t: str) -> str:
        def matches(arr1: List[int], arr2: List[int]) -> bool:
            for i, num in enumerate(arr1):
                if num < arr2[i]:
                    return False
            return True
        if len(t)>len(s):
            return ""
        tCount = [0]*52 # uppercase AND lowercase letters
        sCount = [0]*52
        for char in t:
            if char == char.lower():
                tCount[ord(char)-ord('a')] += 1
            else:
                tCount[ord(char)-ord('A')+26] += 1
        for i in range(len(t)):
            if s[i] == s[i].lower():
                sCount[ord(s[i])-ord('a')] += 1
            else:
                sCount[ord(s[i])-ord('A')+26] += 1
        l = 0
        r = len(t)
        res = len(s)
        leftIndex, rightIndex = 0, 0
        while r <= len(s):
            if matches(sCount,tCount):
                if r-l <= res:
                    leftIndex = l
                    rightIndex = r
                    res = r-l
                if s[l]==s[l].lower():
                    sCount[ord(s[l])-ord('a')] -= 1
                else:
                    sCount[ord(s[l])-ord('A')+26] -=1
                l += 1
            else:
                if r < len(s):
                    if s[r]==s[r].lower():
                        sCount[ord(s[r])-ord('a')] += 1
                    else:
                        sCount[ord(s[r])-ord('A')+26] +=1
                r += 1
        return s[leftIndex:rightIndex]