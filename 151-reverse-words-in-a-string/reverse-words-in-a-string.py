class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()
        right = len(s_split)-1
        left = 0
        while left < right:
            s_split[left] , s_split[right] = s_split[right],s_split[left]
            left += 1
            right -= 1
        return " ".join(s_split)

        