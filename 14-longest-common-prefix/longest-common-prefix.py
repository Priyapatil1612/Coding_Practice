class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_str = min(strs,key = len)
        for i,char in enumerate(short_str):
            for string in strs:
                if string[i] != char:
                    return short_str[:i]
        return short_str
        
        