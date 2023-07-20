class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount, index, n = 0, 0, len(s)
        while index<n:
            count = 0
            subindex = index
            seen = set()
            while subindex<n and s[subindex] not in seen:
                seen.add(s[subindex])
                count += 1
                subindex += 1
            maxCount = max(maxCount, count)
            index += 1
        return maxCount
                
            