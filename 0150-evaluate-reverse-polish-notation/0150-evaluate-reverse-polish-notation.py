class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def interpret(s: str, arg1: int, arg2: int):
            if s == '+':
                return arg1+arg2
            if s == '-':
                return arg1-arg2
            if s == '*':
                return arg1*arg2
            if s == '/':
                return int(arg1/arg2)
                
        stack = []
        for char in tokens:
            if char == '+' or char == '-' or char == '*' or char == '/':
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.append(interpret(char, arg1, arg2))
            else:
                stack.append(int(char))
        return stack.pop()