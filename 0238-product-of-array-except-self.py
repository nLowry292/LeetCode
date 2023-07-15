class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = []
        left.append(nums[0])
        right = []
        right.append(nums[n-1])
        for i in range(1,n-1):
            left.append(left[i-1]*nums[i])
        for j in range(1, n-1):
            right.append(right[j-1]*nums[n-j-1])
        res = []
        res.append(right[n-2])
        print(left)
        print(right)
        for k in range(0, n-2):
            res.append(left[k]*right[n-3-k])
        res.append(left[n-2])
        return res
