class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_cnt = defaultdict(int)
        for i in s:
            char_cnt[i] += 1
        long_len = 0
        for j in list(char_cnt.values()):
            if j % 2 == 0:
                long_len += j
            elif j/2 >= 1:
                long_len = long_len+j - 1 
        if long_len < len(s):
            long_len += 1
            return long_len
        else:
            return long_len