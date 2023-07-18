class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while True:
            sum = numbers[left]+numbers[right]
            if sum < target:
                left = left + 1
                continue
            if sum > target:
                right = right - 1
                continue
            return [left+1,right+1]
            