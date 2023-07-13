class Solution(object):
    def groupAnagrams(self, strs):
        anagramList = defaultdict(list) # sorted char list : list of anagrams
        for str in strs:
            charList = sorted(str)
            anagramList[tuple(charList)].append(str)
        return anagramList.values()
        
