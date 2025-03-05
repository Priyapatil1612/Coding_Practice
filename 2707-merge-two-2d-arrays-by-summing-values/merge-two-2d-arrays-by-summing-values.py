class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        my_dict = {}
        for i in nums1,nums2:
            for j in i:
                if j[0] in my_dict:
                    my_dict[j[0]] += j[1]
                else:
                    my_dict[j[0]] = j[1]
        sorted_dict = dict(sorted(my_dict.items()))
        ans = [[k, v] for k, v in sorted_dict.items()]
        return ans