class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openN: int , closedN: int, string: str):
            if openN == closedN == n:
                res.append(string)
            if openN < n:
                backtrack(openN+1, closedN, string+'(')
            if closedN < openN:
                backtrack(openN, closedN+1, string+')')
        backtrack(0,0, "")
        return res
    
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res = []

#         def backtrack(openN, closedN):
#             if openN == closedN == n:
#                 res.append("".join(stack))
#                 return #this return stops you from running the next two checks, as they are redundant

#             if openN < n:
#                 stack.append("(")
#                 backtrack(openN + 1, closedN)
#                 stack.pop()
#             if closedN < openN:
#                 stack.append(")")
#                 backtrack(openN, closedN + 1)
#                 stack.pop()

#         backtrack(0, 0)
#         return res