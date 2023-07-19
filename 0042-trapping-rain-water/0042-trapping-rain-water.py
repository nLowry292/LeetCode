class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        maxLeft, maxRight = height[0], height[n-1]
        left, right = 0, n-1
        while left < right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])
            if maxLeft <= maxRight:
                res += max(maxLeft-height[left], 0)
                left += 1
            else: #maxLeft>maxRight
                res += max(maxRight-height[right],0)
                right -= 1
        return res
                
            
        
            