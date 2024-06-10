class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_li = sorted(heights)
        incorrect_count = 0
        for i in range(len(heights)):
            if expected_li[i] != heights[i]:
                incorrect_count+=1
        return incorrect_count