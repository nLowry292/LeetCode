class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0]*n
        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                top = stack.pop()
                print(top)
                res[top[1]] = i-top[1]
            stack.append((temp,i))
        return res