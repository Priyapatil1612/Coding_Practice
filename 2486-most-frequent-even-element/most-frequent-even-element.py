class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        countdict = Counter(nums)
        sorted_cntdict = dict(sorted(countdict.items(), key=lambda item: (-item[1], item[0])))
        for k in sorted_cntdict.keys():
            if k % 2 == 0:
                return k
            else:
                continue
        return -1