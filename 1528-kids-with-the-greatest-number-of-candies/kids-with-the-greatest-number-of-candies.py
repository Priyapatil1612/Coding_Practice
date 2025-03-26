class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candi = max(candies)
        ans_list = []
        for i in range(len(candies)):
            ele = candies[i] + extraCandies
            if ele >= max_candi:
                ans_list.append(True)
            else:
                ans_list.append(False)
        return ans_list