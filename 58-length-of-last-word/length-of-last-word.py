class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = s.split()
        ele = li[-1]
        return len(ele)
        