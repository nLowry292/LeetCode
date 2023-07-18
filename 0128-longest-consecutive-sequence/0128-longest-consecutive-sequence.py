class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        setofNums = set(nums)
        maxLength = 1
        currentLength = 1
        for num in nums:
            if num-1 not in setofNums:
                i=1
                while True:
                    if num+i in setofNums:
                        currentLength += 1
                        i += 1
                    else:
                        if currentLength > maxLength:
                            maxLength = currentLength
                        currentLength = 1
                        break
        return maxLength