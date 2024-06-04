class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i in range(len(s)):
            if j<len(t) and s[i] == t[j]:
                j = j+1
            else:
                continue
        return len(t[j:])

        """
                c o a c h i n g
            i.  0 1 2 3 4 5 6 7
                c o d i n g 
            j.  0 1 2

        """