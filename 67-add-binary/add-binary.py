class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = bin(int(a,2)+int(b,2))
        ans = ans[2:]
        return ans