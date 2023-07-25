class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                match = stack.pop()
                if (match == '(' and char != ')') or (match == '{' and char != '}') or (match == '[' and char != ']') :
                    return False
        return len(stack) == 0