class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        items_req = list(range(1,((n ** 2 )+ 1)))
        temp_list = []
        for i in grid:
            for j in i:
                temp_list.append(j)
        hash_cnt = Counter(temp_list)
        for k in hash_cnt.keys():
            if hash_cnt[k] > 1:
                rep_item = k
        avail_items = list(hash_cnt.keys())
        abs_item = None
        for i in items_req:
            if i in avail_items:
                continue
            else:
                abs_item = i
        return [rep_item,abs_item]