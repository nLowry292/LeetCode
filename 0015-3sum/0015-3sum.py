class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)
        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                sum = num+nums[left]+nums[right]
                if sum>0:
                    right = right-1
                elif sum<0:
                    left = left+1
                else:
                    res.append([num,nums[left],nums[right]])
                    left = left+1
                    while nums[left]==nums[left-1] and left<right:
                        left = left+1
                    
        return res