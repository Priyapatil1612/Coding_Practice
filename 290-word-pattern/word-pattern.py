class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split(' ')
        if len(pattern) != len(split_s):
            return False
        
        c2w = {}
        w2c = {}

        for c, w in zip(pattern,split_s):
            if c in c2w and c2w[c] != w:
                return False
            if w in w2c and w2c[w] != c:
                return False

            if c not in c2w and w not in w2c:
                c2w[c] = w
                w2c[w] = c
        return True        