class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_ans = 0
        for k in range(len(s)-1):
            diff = abs(ord(s[k])-ord(s[k+1]))
            sum_ans += diff
        return sum_ans
