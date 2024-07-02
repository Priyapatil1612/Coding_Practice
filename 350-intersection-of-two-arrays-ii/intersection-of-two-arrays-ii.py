class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = Counter(nums1)
        inter_arr = []
        for i in nums2:
            if dict1[i] > 0:
                inter_arr.append(i)
                dict1[i] -= 1
        return inter_arr
