class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s = list(s)
        j = len(list_s) -1
        i = 0
        vowel = "aeiouAEIOU"

        while i < j:
            while i < j and vowel.find(list_s[i]) == -1:
                i += 1
            while i <j and vowel.find(list_s[j]) == -1:
                j -= 1

            list_s[i],list_s[j] = list_s[j],list_s[i]

            i += 1
            j -= 1
        return "".join(list_s)        

        
        