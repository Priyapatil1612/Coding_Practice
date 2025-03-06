class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        temp_list = []
        for i in grid:
            for j in i:
                temp_list.append(j)
        hash_cnt = Counter(temp_list)
        # for k in hash_cnt.keys():
        #     if hash_cnt[k] > 1:
        #         rep_item = k
        # avail_items = list(hash_cnt.keys())
        # abs_item = None
        for i in range(1,n*n+1):
            if i not in hash_cnt:
                abs_item = i
            elif hash_cnt[i] == 2:
                rep_item = i
        return [rep_item,abs_item]