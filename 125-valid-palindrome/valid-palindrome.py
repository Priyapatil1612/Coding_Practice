class Solution:
    import string
    def isPalindrome(self, s: str) -> bool:
        str_l = s.lower()
        str_l = str_l.replace(" ","")
        translator = str.maketrans('','',string.punctuation)
        final_s = str_l.translate(translator)
        left = 0
        right = len(final_s)-1
        while left < right:
            if final_s[left] != final_s[right]:
                return False
            left += 1
            right -= 1
        return True