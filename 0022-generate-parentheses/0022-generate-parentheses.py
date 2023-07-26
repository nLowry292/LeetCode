class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     string = ""
    #     res = []
    #     def backtrack(openN: int , closedN: int):
    #         global string
    #         if openN == closedN == n:
    #             res.append(string)
    #         if openN < n:
    #             "".join([string,'('])
    #             backtrack(openN+1, closedN)
    #             string = string[0:len(string)]
    #         if closedN < openN:
    #             string = string + ')'
    #             backtrack(openN, closedN+1)
    #             string = string[0:len(string)]
    #     backtrack(0,0)
    #     return res
    
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res