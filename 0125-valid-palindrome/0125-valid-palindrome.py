class Solution:
    def isPalindrome(self, s: str) -> bool:
        #ASCII vals for digits are 48-57
        #ASCII vals for uppercase letters are 65-90
        #ASCII vals for lowercase letters are 97-122
        left = 0
        right = len(s)-1
        lst = list(s)
        while (left < right):
            leftCharVal = ord(lst[left])
            rightCharVal = ord(lst[right])
            print("(%s,%s,%d,%d)", lst[left], lst[right],leftCharVal,rightCharVal)
            if leftCharVal not in range(48,58) and leftCharVal not in range(65,91) and leftCharVal not in range(97,123):
                left = left+1
                continue
            if rightCharVal not in range(48,58) and rightCharVal not in range(65,91) and rightCharVal not in range(97,123):
                right = right-1
                continue
            if leftCharVal in range(97,123) and rightCharVal in range(65,91):
                if leftCharVal != rightCharVal + 32:
                    return False
            elif leftCharVal in range(65,91) and rightCharVal in range(97,123):
                    if leftCharVal + 32 != rightCharVal:
                        return False
            elif leftCharVal != rightCharVal:
                    return False
            
            left = left+1
            right = right-1
        return True
                