class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        temp_list = {}
        for i in grid:
            for j in i:
                temp_list[j] = temp_list.get(j,0)+1
        for i in range(1,n*n+1):
            if i not in temp_list:
                abs_item = i
            elif temp_list[i] == 2:
                rep_item = i
        return [rep_item,abs_item]