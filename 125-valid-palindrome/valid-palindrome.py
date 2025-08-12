class Solution:
    import string
    def isPalindrome(self, s: str) -> bool:
        ## Two POINTER APPROACH -----> O(n^2)

        # lower_s = s.lower()
        # new_s = ""
        # for char in lower_s:
        #     if char.isalnum():
        #         new_s += char
        #         i = 0
        #         j = len(new_s) - 1
        #         while i <= j:
        #             if new_s[i] != new_s[j]:
        #                 return False
        #             i += 1
        #             j -= 1
        #         return True
        
        ## REVERSE STRING  ------------>O(n)
        new_s = ''.join(c.lower() for c in s if c.isalnum())
        if new_s == new_s[::-1]:
            return True
        return False


        




















