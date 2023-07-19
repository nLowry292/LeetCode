class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxArea, currentArea, left, right = 0, 0, 0, n-1
        while left<right:
            currentArea = (right-left)*min(height[left],height[right])
            if currentArea > maxArea:
                maxArea = currentArea
            if height[left]<=height[right]:
                left += 1
            else:
                right -=1
        return maxArea
            
        