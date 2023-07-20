class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount, index, n = 0, 0, len(s)
        while index<n:
            count = 0
            subindex = index
            seen = {} # character -> index
            while subindex<n and s[subindex] not in seen:
                seen[s[subindex]] = subindex
                count += 1
                subindex += 1
            maxCount = max(maxCount, count)
            if subindex == n:
                return maxCount
            index = seen[s[subindex]]+1
        return maxCount
                
            