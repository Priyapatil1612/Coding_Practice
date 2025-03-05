class Solution:
    def coloredCells(self, n: int) -> int:
        x = n-1
        ans = 1+4*(x*(x+1))/2
        return int(ans)