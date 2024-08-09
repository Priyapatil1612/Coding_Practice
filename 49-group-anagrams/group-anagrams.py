class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            charcnt = [0]*26
            for char in s:
                charcnt[ord(char)-ord("a")] += 1
            result[tuple(charcnt)].append(s)
        return result.values()
        