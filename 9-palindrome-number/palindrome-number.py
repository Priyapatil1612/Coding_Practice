class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_s = str(x)
        left = 0
        right = len(x_s)-1
        while left < right:
            if x_s[left] != x_s[right]:
                return False
            left += 1
            right -= 1
        return True