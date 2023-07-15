class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqTable = {}
        for num in nums:
            freqTable[num] = freqTable.get(num,0) + 1
        pairs = sorted(freqTable.items(), key = lambda x:x[1],)
        print(pairs)
        lst = []
        n = len(pairs)
        for i in range(k):
            lst.append(pairs[n-i-1][0])
        return lst
