class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest, res = prices[0], 0
        for num in prices:
            smallest = min(smallest, num)
            res = max(res, num-smallest)
        return res