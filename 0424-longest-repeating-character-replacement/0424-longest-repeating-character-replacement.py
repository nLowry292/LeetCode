class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, maxfreq, n = 0, 0, len(s)
        count = {}
        for right in range(n):
            count[s[right]] = count.get(s[right],0) + 1
            maxfreq = max(maxfreq, count[s[right]])
            if (right-left+1 - maxfreq > k):
                count[s[left]] -= 1
                left += 1
        return right-left+1
            